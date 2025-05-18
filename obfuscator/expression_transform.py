import random
from obfuscator.ast import *

class ExpressionTransformer:
    def transform(self, node):
        if isinstance(node, Program):
            for func in node.functions:
                self.transform(func)

        elif isinstance(node, Function):
            for stmt in node.body:
                self.transform(stmt)

        elif isinstance(node, Block):
            for stmt in node.items:
                self.transform(stmt)

        elif isinstance(node, IfStmt):
            self.transform(node.condition)
            self.transform(node.then_branch)
            if node.else_branch:
                self.transform(node.else_branch)

        elif isinstance(node, WhileStmt):
            self.transform(node.condition)
            self.transform(node.body)

        elif isinstance(node, ForStmt):
            if node.init:
                self.transform(node.init)
            if node.cond:
                self.transform(node.cond)
            if node.update:
                self.transform(node.update)
            self.transform(node.body)

        elif isinstance(node, Return):
            if node.value:
                self.transform(node.value)

        elif isinstance(node, ExpressionStmt):
            if node.expr:
                self.transform(node.expr)

        elif isinstance(node, Assignment):
            self.transform(node.value)

        elif isinstance(node, Print):
            for i in range(len(node.args)):
                self.transform(node.args[i])

        elif isinstance(node, UnaryOp):
            node.operand = self.transform(node.operand)
            node = self.rewrite_unary(node)
            return node

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
        if node.op == '+':
            # a + b → a - (-b)
            if random.random() < 0.6:
                return BinaryOp('-', node.left, UnaryOp('-', node.right))

        elif node.op == '-':
            # a - b → a + (-b)
            if random.random() < 0.6:
                return BinaryOp('+', node.left, UnaryOp('-', node.right))

        elif node.op == '*':
            # a * 2 → a + a
            if isinstance(node.right, Literal) and node.right.value == 2:
                return BinaryOp('+', node.left, node.left)

        elif node.op == '==':
            # a == b → !(a != b)
            if random.random() < 0.5:
                inner = BinaryOp('!=', node.left, node.right)
                return UnaryOp('!', inner)

        return node

    def rewrite_unary(self, node):
        if node.op == '-' and isinstance(node.operand, Variable):
            if random.random() < 0.5:
                return BinaryOp('-', Literal(0), node.operand)
        return node