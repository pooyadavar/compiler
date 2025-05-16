from typing import List, Optional

class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, functions: List['Function']):
        self.functions = functions

class Function(ASTNode):
    def __init__(self, return_type: str, name: str, params: List['Parameter'], body: List['Statement']):
        self.return_type = return_type
        self.name = name
        self.params = params
        self.body = body

class Parameter(ASTNode):
    def __init__(self, param_type: str, name: str):
        self.param_type = param_type
        self.name = name

class VariableDecl(ASTNode):
    def __init__(self, var_type: str, name: str, init_expr: Optional['Expression']):
        self.var_type = var_type
        self.name = name
        self.init_expr = init_expr

class Return(ASTNode):
    def __init__(self, value: Optional['Expression']):
        self.value = value

class ExpressionStmt(ASTNode):
    def __init__(self, expr: Optional['Expression']):
        self.expr = expr

class IfStmt(ASTNode):
    def __init__(self, condition: 'Expression', then_branch: 'Statement', else_branch: Optional['Statement']):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

class WhileStmt(ASTNode):
    def __init__(self, condition: 'Expression', body: 'Statement'):
        self.condition = condition
        self.body = body

class ForStmt(ASTNode):
    def __init__(self, init: Optional['Expression'], cond: Optional['Expression'], update: Optional['Expression'], body: 'Statement'):
        self.init = init
        self.cond = cond
        self.update = update
        self.body = body

class Block(ASTNode):
    def __init__(self, items: List['Statement']):
        self.items = items

class Print(ASTNode):
    def __init__(self, format_str: str, args: List['Expression']):
        self.format_str = format_str
        self.args = args

class Scan(ASTNode):
    def __init__(self, format_str: str, args: List[str]):
        self.format_str = format_str
        self.args = args

class Assignment(ASTNode):
    def __init__(self, target: str, value: 'Expression'):
        self.target = target
        self.value = value

# --- Expressions ---

class Expression(ASTNode):
    pass

class BinaryOp(Expression):
    def __init__(self, op: str, left: Expression, right: Expression):
        self.op = op
        self.left = left
        self.right = right

class UnaryOp(Expression):
    def __init__(self, op: str, operand: Expression):
        self.op = op
        self.operand = operand

class Literal(Expression):
    def __init__(self, value):
        self.value = value

class Variable(Expression):
    def __init__(self, name: str):
        self.name = name

class FuncCall(Expression):
    def __init__(self, name: str, args: List[Expression]):
        self.name = name
        self.args = args

class Statement(ASTNode):
    pass
