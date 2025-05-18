from obfuscator.ast import *

class CodeGenerator:
    def __init__(self):
        self.output = []

    def generate(self, node):
        self.visit(node)
        return '\n'.join(self.output)

    def emit(self, line):
        self.output.append(line)

    def visit(self, node):
        if isinstance(node, Program):
            for func in node.functions:
                self.visit(func)

        elif isinstance(node, Function):
            params = ', '.join([f"{p.param_type} {p.name}" for p in node.params])
            self.emit(f"{node.return_type} {node.name}({params}) {{")
            for stmt in node.body:
                self.visit(stmt)
            self.emit("}")

        elif isinstance(node, VariableDecl):
            line = f"{node.var_type} {node.name}"
            if node.init_expr:
                line += f" = {self.visit_expr(node.init_expr)}"
            self.emit(line + ";")

        elif isinstance(node, Assignment):
            self.emit(f"{node.target} = {self.visit_expr(node.value)};")

        elif isinstance(node, ExpressionStmt):
            if node.expr:
                self.emit(f"{self.visit_expr(node.expr)};")
            else:
                self.emit(";")

        elif isinstance(node, Return):
            if node.value:
                self.emit(f"return {self.visit_expr(node.value)};")
            else:
                self.emit("return;")

        elif isinstance(node, IfStmt):
            cond = self.visit_expr(node.condition)
            self.emit(f"if ({cond})")
            self.visit(node.then_branch)
            if node.else_branch:
                self.emit("else")
                self.visit(node.else_branch)

        elif isinstance(node, WhileStmt):
            cond = self.visit_expr(node.condition)
            self.emit(f"while ({cond})")
            self.visit(node.body)

        elif isinstance(node, ForStmt):
            init = self.visit_expr(node.init) if node.init else ''
            cond = self.visit_expr(node.cond) if node.cond else ''
            update = self.visit_expr(node.update) if node.update else ''
            self.emit(f"for ({init}; {cond}; {update})")
            self.visit(node.body)

        elif isinstance(node, Block):
            self.emit("{")
            for stmt in node.items:
                self.visit(stmt)
            self.emit("}")

        elif isinstance(node, Print):
            args = ', '.join([self.visit_expr(a) for a in node.args])
            self.emit(f'printf("{node.format_str}", {args});')

        elif isinstance(node, Scan):
            args = ', '.join(['&' + a for a in node.args])
            self.emit(f'scanf("{node.format_str}", {args});')

    def visit_expr(self, expr):
        if isinstance(expr, Literal):
            if isinstance(expr.value, str):
                return f'"{expr.value}"'
            elif isinstance(expr.value, bool):
                return "true" if expr.value else "false"
            else:
                return str(expr.value)

        elif isinstance(expr, Variable):
            return expr.name

        elif isinstance(expr, FuncCall):
            args = ', '.join([self.visit_expr(arg) for arg in expr.args])
            return f"{expr.name}({args})"

        elif isinstance(expr, BinaryOp):
            left = self.visit_expr(expr.left)
            right = self.visit_expr(expr.right)
            return f"({left} {expr.op} {right})"

        elif isinstance(expr, UnaryOp):
            operand = self.visit_expr(expr.operand)
            return f"({expr.op}{operand})"