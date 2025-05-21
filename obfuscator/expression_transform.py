import random
from obfuscator.ast import *

class ExpressionTransformer:
    def transform(self, node):
        if isinstance(node, Program):
            for i in range(len(node.functions)):
                node.functions[i] = self.transform(node.functions[i])

        elif isinstance(node, Function):
            for i in range(len(node.body)):
                node.body[i] = self.transform(node.body[i])
        
        elif isinstance(node, VariableDecl):
            if node.init_expr:
                node.init_expr = self.transform(node.init_expr)

        elif isinstance(node, Block):
            for i in range(len(node.items)):
                node.items[i] = self.transform(node.items[i])

        elif isinstance(node, IfStmt):
            node.condition = self.transform(node.condition)
            node.then_branch = self.transform(node.then_branch)
            if node.else_branch:
                node.else_branch = self.transform(node.else_branch)

        elif isinstance(node, WhileStmt):
            node.condition = self.transform(node.condition)
            node.body = self.transform(node.body)

        elif isinstance(node, ForStmt):
            if node.init:
                node.init = self.transform(node.init)
            if node.cond:
                node.cond = self.transform(node.cond)
            if node.update:
                node.update = self.transform(node.update)
            node.body = self.transform(node.body)

        elif isinstance(node, Return):
            if node.value:
                node.value = self.transform(node.value)

        elif isinstance(node, ExpressionStmt):
            if node.expr:
                node.expr = self.transform(node.expr)

        elif isinstance(node, Assignment):
            node.value = self.transform(node.value)

        elif isinstance(node, Print):
            for i in range(len(node.args)):
                node.args[i] = self.transform(node.args[i])

        elif isinstance(node, UnaryOp):
            node.operand = self.transform(node.operand)
            return self.rewrite_unary(node)

        elif isinstance(node, BinaryOp):
            node.left = self.transform(node.left)
            node.right = self.transform(node.right)
            return self.rewrite_binary(node)

        elif isinstance(node, FuncCall):
            for i in range(len(node.args)):
                node.args[i] = self.transform(node.args[i])

        elif isinstance(node, Variable) or isinstance(node, Literal):
            return node

        return node

    def rewrite_binary(self, node):
        #print("flag1")
        if node.op == '+':
            # a + b → a - (-b)
            # if random.random() < 1.0:
            return BinaryOp('-', node.left, UnaryOp('-', node.right))

        elif node.op == '-':
            # a - b → a + (-b)
            if random.random() < 1.0:
                return BinaryOp('+', node.left, UnaryOp('-', node.right))

        elif node.op == '*':
            # a * 2 → a + a
            if isinstance(node.right, Literal) and node.right.value == 2:
                return BinaryOp('+', node.left, node.left)

        elif node.op == '==':
            # a == b → !(a != b)
            if random.random() < 1.0:
                inner = BinaryOp('!=', node.left, node.right)
                return UnaryOp('!', inner)

        return node

    def rewrite_unary(self, node):
        if node.op == '-' and isinstance(node.operand, Variable):
            if random.random() < 1.0:
                return BinaryOp('-', Literal(0), node.operand)
        return node