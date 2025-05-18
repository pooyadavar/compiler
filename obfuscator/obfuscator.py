import random
import string
from obfuscator.ast import *

class NameObfuscator:
    def __init__(self):
        self.name_map = {}
        self.used_names = set()

    def generate_name(self):
        while True:
            name = ''.join(random.choices(string.ascii_lowercase, k=3)) + str(random.randint(1, 99))
            if name not in self.used_names:
                self.used_names.add(name)
                return name

    def obfuscate(self, node):
        if isinstance(node, Program):
            for func in node.functions:
                self.obfuscate(func)

        elif isinstance(node, Function):
            orig_name = node.name
            if orig_name not in self.name_map:
                self.name_map[orig_name] = self.generate_name()
            node.name = self.name_map[orig_name]

            for param in node.params:
                self.obfuscate(param)

            for stmt in node.body:
                self.obfuscate(stmt)

        elif isinstance(node, Parameter):
            if node.name not in self.name_map:
                self.name_map[node.name] = self.generate_name()
            node.name = self.name_map[node.name]

        elif isinstance(node, VariableDecl):
            if node.name not in self.name_map:
                self.name_map[node.name] = self.generate_name()
            node.name = self.name_map[node.name]
            if node.init_expr:
                self.obfuscate(node.init_expr)

        elif isinstance(node, Assignment):
            if node.target in self.name_map:
                node.target = self.name_map[node.target]
            self.obfuscate(node.value)

        elif isinstance(node, Return):
            if node.value:
                self.obfuscate(node.value)

        elif isinstance(node, ExpressionStmt):
            if node.expr:
                self.obfuscate(node.expr)

        elif isinstance(node, IfStmt):
            self.obfuscate(node.condition)
            self.obfuscate(node.then_branch)
            if node.else_branch:
                self.obfuscate(node.else_branch)

        elif isinstance(node, WhileStmt):
            self.obfuscate(node.condition)
            self.obfuscate(node.body)

        elif isinstance(node, ForStmt):
            if node.init:
                self.obfuscate(node.init)
            if node.cond:
                self.obfuscate(node.cond)
            if node.update:
                self.obfuscate(node.update)
            self.obfuscate(node.body)

        elif isinstance(node, Block):
            for stmt in node.items:
                self.obfuscate(stmt)

        elif isinstance(node, Print):
            for arg in node.args:
                self.obfuscate(arg)

        elif isinstance(node, Scan):
            for i, arg in enumerate(node.args):
                if arg in self.name_map:
                    node.args[i] = self.name_map[arg]

        elif isinstance(node, BinaryOp):
            self.obfuscate(node.left)
            self.obfuscate(node.right)

        elif isinstance(node, UnaryOp):
            self.obfuscate(node.operand)

        elif isinstance(node, FuncCall):
            if node.name in self.name_map:
                node.name = self.name_map[node.name]
            for arg in node.args:
                self.obfuscate(arg)

        elif isinstance(node, Variable):
            if node.name in self.name_map:
                node.name = self.name_map[node.name]

        elif isinstance(node, Literal):
            pass  # هیچ کاری لازم نیست