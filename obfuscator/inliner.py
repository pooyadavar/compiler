from obfuscator.ast import *
import copy
import itertools

class FunctionInliner:
    def __init__(self, ast: Program):
        self.ast = ast
        self.function_map = {func.name: func for func in ast.functions}
        self.counter = itertools.count()

    def inline(self):
        for func in self.ast.functions:
            func.body = self._inline_block(func.body)

    def _inline_block(self, stmts: List[Statement]) -> List[Statement]:
        result = []
        for stmt in stmts:
            if isinstance(stmt, ExpressionStmt) and isinstance(stmt.expr, FuncCall):
                inlined = self._try_inline_call(stmt.expr)
                if inlined:
                    result.extend(inlined)
                    continue
            elif isinstance(stmt, VariableDecl) and isinstance(stmt.init_expr, FuncCall):
                inlined = self._try_inline_call(stmt.init_expr, assign_to=stmt.name)
                if inlined:
                    result.extend(inlined)
                    continue
            elif isinstance(stmt, IfStmt):
                stmt.then_branch = self._wrap(stmt.then_branch)
                if stmt.else_branch:
                    stmt.else_branch = self._wrap(stmt.else_branch)
            elif isinstance(stmt, WhileStmt):
                stmt.body = self._wrap(stmt.body)
            elif isinstance(stmt, ForStmt):
                stmt.body = self._wrap(stmt.body)
            elif isinstance(stmt, Block):
                stmt.items = self._inline_block(stmt.items)
            result.append(stmt)
        return result

    def _wrap(self, s):
        if isinstance(s, Block):
            return Block(self._inline_block(s.items))
        return Block(self._inline_block([s]))

    def _try_inline_call(self, call: FuncCall, assign_to=None) -> Optional[List[Statement]]:
        target_func = self.function_map.get(call.name)
        if not target_func:
            return None

        # avoid inlining recursive calls for now
        if call.name == assign_to:
            return None

        inlined_stmts = []

        param_names = []
        arg_values = call.args
        param_mapping = {}

        for param, arg in zip(target_func.params, arg_values):
            fresh_name = self._fresh_name(param.name)
            param_names.append(fresh_name)
            param_mapping[param.name] = fresh_name  # 💡 map old name to new name
            inlined_stmts.append(VariableDecl(param.param_type, fresh_name, arg))

        body_copy = copy.deepcopy(target_func.body)
        renamer = _LocalVarRenamer(self.counter, param_mapping)
        body_copy = renamer.rename_block(body_copy, param_names)

        temp_result = self._fresh_name("ret") if assign_to is None else assign_to
        final_stmts = []
        for stmt in body_copy:
            if isinstance(stmt, Return):
                if stmt.value:
                    final_stmts.append(Assignment(Variable(temp_result), stmt.value))
            else:
                final_stmts.append(stmt)

        if assign_to is None:
            inlined_stmts.append(ExpressionStmt(Variable(temp_result)))
        else:
            pass

        inlined_stmts.extend(final_stmts)
        return inlined_stmts

    def _fresh_name(self, base):
        return f"{base}_{next(self.counter)}"

class _LocalVarRenamer:
    def __init__(self, counter, initial_map=None):
        self.counter = counter
        self.name_map = initial_map or {} 

    def rename_block(self, stmts: List[Statement], exclude: List[str] = []) -> List[Statement]:
        renamed = []
        for stmt in stmts:
            renamed.append(self._rename_stmt(stmt, exclude))
        return renamed

    def _rename_stmt(self, stmt: Statement, exclude: List[str]) -> Statement:
        if isinstance(stmt, VariableDecl):
            if stmt.name not in exclude:
                new_name = self._fresh(stmt.name)
                self.name_map[stmt.name] = new_name
                stmt.name = new_name
            if stmt.init_expr:
                stmt.init_expr = self._rename_expr(stmt.init_expr)
        elif isinstance(stmt, Assignment):
            stmt.target = Variable(self._map(stmt.target))
            stmt.value = self._rename_expr(stmt.value)
        elif isinstance(stmt, ExpressionStmt):
            if stmt.expr:
                stmt.expr = self._rename_expr(stmt.expr)
        elif isinstance(stmt, Return):
            if stmt.value:
                stmt.value = self._rename_expr(stmt.value)
        elif isinstance(stmt, IfStmt):
            stmt.condition = self._rename_expr(stmt.condition)
            stmt.then_branch = self._rename_stmt(stmt.then_branch, exclude)
            if stmt.else_branch:
                stmt.else_branch = self._rename_stmt(stmt.else_branch, exclude)
        elif isinstance(stmt, WhileStmt):
            stmt.condition = self._rename_expr(stmt.condition)
            stmt.body = self._rename_stmt(stmt.body, exclude)
        elif isinstance(stmt, ForStmt):
            if stmt.init:
                stmt.init = self._rename_expr(stmt.init)
            if stmt.cond:
                stmt.cond = self._rename_expr(stmt.cond)
            if stmt.update:
                stmt.update = self._rename_expr(stmt.update)
            stmt.body = self._rename_stmt(stmt.body, exclude)
        elif isinstance(stmt, Block):
            stmt.items = self.rename_block(stmt.items, exclude)
        return stmt

    def _rename_expr(self, expr: Expression) -> Expression:
        if isinstance(expr, Variable):
            return Variable(self._map(expr.name))
        elif isinstance(expr, BinaryOp):
            return BinaryOp(expr.op, self._rename_expr(expr.left), self._rename_expr(expr.right))
        elif isinstance(expr, UnaryOp):
            return UnaryOp(expr.op, self._rename_expr(expr.operand))
        elif isinstance(expr, FuncCall):
            return FuncCall(expr.name, [self._rename_expr(arg) for arg in expr.args])
        elif isinstance(expr, Literal):
            return expr
        else:
            return expr

    def _map(self, name):
        return self.name_map.get(name, name)

    def _fresh(self, name):
        return f"{name}_{next(self.counter)}"
