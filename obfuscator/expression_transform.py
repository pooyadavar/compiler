from obfuscator.ast import *
import random

class ExpressionTransformer:
    def transform(self, node):
        if isinstance(node, Program):
            for i in range(len(node.functions)):
                node.functions[i] = self.transform(node.functions[i])
        elif isinstance(node, Function):
            for i in range(len(node.body)):
                node.body[i] = self.transform(node.body[i])

        elif isinstance(node, Block):
            for i in range(len(node.items)):
                node.items[i] = self.transform(node.items[i])

        elif isinstance(node, VariableDecl):
            if node.init_expr:
                node.init_expr = self._transform_expr(node.init_expr)

        elif isinstance(node, Assignment):
            node.value = self._transform_expr(node.value)

        elif isinstance(node, ExpressionStmt):
            if node.expr:
                node.expr = self._transform_expr(node.expr)

        elif isinstance(node, IfStmt):
            node.condition = self._transform_expr(node.condition)
            node.then_branch = self.transform(node.then_branch)
            if node.else_branch:
                node.else_branch = self.transform(node.else_branch)

        elif isinstance(node, WhileStmt):
            node.condition = self._transform_expr(node.condition)
            node.body = self.transform(node.body)

        elif isinstance(node, ForStmt):
            if node.init:
                node.init = self.transform(node.init)
            if node.cond:
                node.cond = self._transform_expr(node.cond)
            if node.update:
                node.update = self.transform(node.update)
            node.body = self.transform(node.body)

        elif isinstance(node, Return):
            if node.value:
                node.value = self._transform_expr(node.value)

        elif isinstance(node, Print):
            for i in range(len(node.args)):
                node.args[i] = self._transform_expr(node.args[i])

        return node

    def _transform_expr(self, expr):
        if isinstance(expr, BinaryOp):
            expr.left = self._transform_expr(expr.left)
            expr.right = self._transform_expr(expr.right)
            return self.rewrite_binary(expr)

        elif isinstance(expr, UnaryOp):
            expr.operand = self._transform_expr(expr.operand)
            return self.rewrite_unary(expr)

        elif isinstance(expr, Assignment):
            expr.value = self._transform_expr(expr.value)
            return expr

        elif isinstance(expr, FuncCall):
            for i in range(len(expr.args)):
                expr.args[i] = self._transform_expr(expr.args[i])
            return expr

        elif isinstance(expr, Variable) or isinstance(expr, Literal):
            return expr

        return expr

    def rewrite_binary(self, node):
        if node.op == '+':
            return BinaryOp('-', node.left, UnaryOp('-', node.right))

        elif node.op == '-':
            return BinaryOp('+', node.left, UnaryOp('-', node.right))

        elif node.op == '*':
            if isinstance(node.right, Literal) and node.right.value == 2:
                return BinaryOp('+', node.left, node.left)

        elif node.op == '==':
            inner = BinaryOp('!=', node.left, node.right)
            return UnaryOp('!', inner)

        return node

    def rewrite_unary(self, node):
        if node.op == '-' and isinstance(node.operand, Variable):
            return BinaryOp('-', Literal(0), node.operand)
        return node
