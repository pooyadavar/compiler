import random
from obfuscator.ast import *

class DeadCodeInserter:
    def __init__(self):
        self.counter = 0

    def insert(self, node):
        if isinstance(node, Program):
            for func in node.functions:
                self.insert(func)

        elif isinstance(node, Function):
            new_body = []
            for stmt in node.body:
                if random.random() < 0.3: 
                    new_body.append(self.make_dead_stmt())
                self.insert(stmt)
                new_body.append(stmt)
            node.body = new_body

        elif isinstance(node, Block):
            new_items = []
            for stmt in node.items:
                if random.random() < 0.3:
                    new_items.append(self.make_dead_stmt())
                self.insert(stmt)
                new_items.append(stmt)
            node.items = new_items

        elif isinstance(node, IfStmt):
            self.insert(node.then_branch)
            if node.else_branch:
                self.insert(node.else_branch)

        elif isinstance(node, WhileStmt):
            self.insert(node.body)

        elif isinstance(node, ForStmt):
            self.insert(node.body)

    def make_dead_stmt(self):
        kind = random.choice(["var", "if"])

        if kind == "var":
            var_name = f"unused_{self.counter}"
            self.counter += 1
            return VariableDecl("int", var_name, Literal(random.randint(100, 999)))

        elif kind == "if":
            return IfStmt(
                condition=Literal(0),
                then_branch=Block([
                    ExpressionStmt(
                        FuncCall("printf", [Literal("Unreachable\\n")])
                    )
                ]),
                else_branch=None
            )