import random
import string
from typing import Dict, Set, Union, List
from obfuscator.ast import *


class NameObfuscator:
    """Obfuscates variable and function names in the AST, preserving 'main'."""

    def __init__(self):
        self.name_map: Dict[str, str] = {}  # Maps original names to obfuscated names
        self.used_names: Set[str] = set()  # Tracks used obfuscated names
        self.scope_stack: List[Set[str]] = [set()]  # Tracks names in current scope

    def generate_name(self) -> str:
        """Generates a unique random name (e.g., xyz12)."""
        while True:
            name = "".join(random.choices(string.ascii_lowercase, k=3)) + str(
                random.randint(1, 999)
            )
            if name not in self.used_names and name not in self.name_map.values():
                self.used_names.add(name)
                self.scope_stack[-1].add(name)
                return name

    def enter_scope(self):
        """Enters a new scope for variable naming."""
        self.scope_stack.append(set())

    def exit_scope(self):
        """Exits the current scope, removing its names."""
        self.scope_stack.pop()

    def obfuscate(self, program: Program) -> None:
        """Obfuscates names in the given AST program."""
        for func in program.functions:
            self.enter_scope()
            self._obfuscate_function(func)
            self.exit_scope()

    def _obfuscate_function(self, func: Function) -> None:
        """Obfuscates function name (except 'main') and its contents."""
        if func.name != "main":
            self._rename(func, "name")
        for param in func.params:
            self._obfuscate_parameter(param)
        self._obfuscate_block(func.body)

    def _obfuscate_parameter(self, param: Parameter) -> None:
        """Obfuscates parameter name."""
        self._rename(param, "name")
        if hasattr(param, "init_expr") and param.init_expr:
            self._obfuscate_expression(param.init_expr)

    def _obfuscate_block(self, block: Union[List[ASTNode], Block]) -> None:
        """Obfuscates all statements in a block or list of statements."""
        if isinstance(block, list):
            for stmt in block:
                self._obfuscate_stmt(stmt)
        elif isinstance(block, Block):
            for stmt in block.items:
                self._obfuscate_stmt(stmt)

    def _obfuscate_stmt(self, stmt: ASTNode) -> None:
        """Obfuscates a statement based on its type."""
        if isinstance(stmt, VariableDecl):
            self._rename(stmt, "name")
            if hasattr(stmt, "init_expr") and stmt.init_expr:
                self._obfuscate_expression(stmt.init_expr)
        elif isinstance(stmt, Assignment):
            if isinstance(stmt.target, Variable) and stmt.target.name in self.name_map:
                stmt.target.name = self.name_map[stmt.target.name]
            self._obfuscate_expression(stmt.value)
        elif isinstance(stmt, Return):
            if stmt.value:
                self._obfuscate_expression(stmt.value)
        elif isinstance(stmt, ExpressionStmt):
            if stmt.expr:
                self._obfuscate_expression(stmt.expr)
        elif isinstance(stmt, IfStmt):
            self.enter_scope()
            self._obfuscate_expression(stmt.condition)
            self._obfuscate_block(stmt.then_branch)
            self.exit_scope()
            if stmt.else_branch:
                self.enter_scope()
                self._obfuscate_block(stmt.else_branch)
                self.exit_scope()
        elif isinstance(stmt, WhileStmt):
            self.enter_scope()
            self._obfuscate_expression(stmt.condition)
            self._obfuscate_block(stmt.body)
            self.exit_scope()
        elif isinstance(stmt, ForStmt):
            self.enter_scope()
            if stmt.init:
                self._obfuscate_stmt(stmt.init)
            if stmt.cond:
                self._obfuscate_expression(stmt.cond)
            if stmt.update:
                self._obfuscate_stmt(stmt.update)
            self._obfuscate_block(stmt.body)
            self.exit_scope()
        elif isinstance(stmt, Print):
            for arg in stmt.args:
                self._obfuscate_expression(arg)
        elif isinstance(stmt, Scan):
            for i, arg in enumerate(stmt.args):
                if isinstance(arg, str) and arg in self.name_map:
                    stmt.args[i] = self.name_map[arg]
                elif isinstance(arg, Variable):
                    self._obfuscate_expression(arg)
        elif isinstance(stmt, Block):
            self.enter_scope()
            self._obfuscate_block(stmt)
            self.exit_scope()

    def _obfuscate_expression(self, expr: ASTNode) -> None:
        """Obfuscates an expression based on its type."""
        if isinstance(expr, Variable):
            if expr.name in self.name_map:
                expr.name = self.name_map[expr.name]
        elif isinstance(expr, BinaryOp):
            self._obfuscate_expression(expr.left)
            self._obfuscate_expression(expr.right)
        elif isinstance(expr, UnaryOp):
            self._obfuscate_expression(expr.operand)
        elif isinstance(expr, FuncCall):
            if expr.name in self.name_map:
                expr.name = self.name_map[expr.name]
            for arg in expr.args:
                self._obfuscate_expression(arg)
        elif isinstance(expr, Literal):
            pass
        elif hasattr(expr, "__dict__"):
            for val in expr.__dict__.values():
                if isinstance(val, ASTNode):
                    self._obfuscate_expression(val)
                elif isinstance(val, list):
                    for item in val:
                        if isinstance(item, ASTNode):
                            self._obfuscate_expression(item)

    def _rename(self, node: ASTNode, name_attr: str) -> None:
        """Renames a node's name attribute if it exists."""
        if hasattr(node, name_attr):
            old_name = getattr(node, name_attr)
            if old_name not in self.name_map:
                self.name_map[old_name] = self.generate_name()
            setattr(node, name_attr, self.name_map[old_name])
