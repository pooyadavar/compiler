from obfuscator.ast import *
from itertools import count
from typing import List


class ControlFlowFlattener:
    id_counter = count()

    def flatten(self, program: Program):
        for i, func in enumerate(program.functions):
            program.functions[i] = self._flatten_function(func)

    def _flatten_function(self, func: Function):
        if not func.body:
            return func

        func_id = next(self.id_counter)
        prefix = f"_f{func_id}"
        state_var = f"{prefix}_state"
        dispatcher_label_name = f"{prefix}_dispatcher"
        end_label_name = f"{prefix}_end"

        # Collect all variables (declared, assigned, or used)
        all_vars = self.collect_all_variables(func.body)
        returned_vars = self.collect_returned_variable_names(func.body)

        # Initialize state variable to 0
        state_decl = VariableDecl("int", state_var, Literal(0))
        new_body = [state_decl]

        for var in sorted(all_vars.union(returned_vars)):
            new_body.append(VariableDecl("int", var, None))

        dispatcher_cases = []
        case_bodies = []

        for i, stmt in enumerate(func.body):
            case_label_name = f"{prefix}_case_{i}"
            label = Label(case_label_name)
            case_body = []

            if isinstance(stmt, VariableDecl):
                init = (
                    getattr(stmt, "init_expr", None)
                    or getattr(stmt, "init", None)
                    or getattr(stmt, "value", None)
                    or getattr(stmt, "initializer", None)
                )
                if init is not None:
                    case_body.append(Assignment(Variable(stmt.name), init))
            elif isinstance(stmt, Assignment):
                case_body.append(stmt)
            elif isinstance(stmt, ExpressionStmt) and isinstance(stmt.expr, FuncCall):
                case_body.append(stmt)
            elif isinstance(stmt, ForStmt):
                init = stmt.init
                loop_var = None
                if isinstance(init, VariableDecl):
                    loop_var = init.name
                    if init.init_expr:
                        case_body.append(Assignment(Variable(loop_var), init.init_expr))
                elif isinstance(init, Assignment):
                    if isinstance(init.target, Variable):
                        loop_var = init.target.name
                    case_body.append(init)
                elif isinstance(init, ExpressionStmt) and isinstance(
                    init.expr, Assignment
                ):
                    if isinstance(init.expr.target, Variable):
                        loop_var = init.expr.target.name
                    case_body.append(init.expr)

                cond = stmt.cond
                update = stmt.update
                if loop_var:
                    if isinstance(cond, BinaryOp) and isinstance(cond.left, Variable):
                        cond.left = Variable(loop_var)
                    if isinstance(update, Assignment) and isinstance(
                        update.target, Variable
                    ):
                        update.target = Variable(loop_var)
                        if isinstance(update.value, BinaryOp) and isinstance(
                            update.value.left, Variable
                        ):
                            update.value.left = Variable(loop_var)
                    elif isinstance(update, ExpressionStmt) and isinstance(
                        update.expr, Assignment
                    ):
                        update.expr.target = Variable(loop_var)
                        if isinstance(update.expr.value, BinaryOp) and isinstance(
                            update.expr.value.left, Variable
                        ):
                            update.expr.value.left = Variable(loop_var)
                case_body.append(
                    ForStmt(init=None, cond=cond, update=update, body=stmt.body)
                )
            elif isinstance(stmt, WhileStmt):
                case_body.append(WhileStmt(condition=stmt.condition, body=stmt.body))
            else:
                case_body.append(stmt)

            if not isinstance(stmt, Return):
                case_body.append(Assignment(Variable(state_var), Literal(i + 1)))
                case_body.append(Goto(dispatcher_label_name))

            dispatcher_cases.append(SwitchCase(Literal(i), label, None))
            case_bodies.append(Block([label] + case_body))

        end_label = Label(end_label_name)
        dispatcher_cases.append(SwitchCase(Literal(len(func.body)), end_label, None))
        case_bodies.append(Block([end_label, Return(Literal(0))]))

        dispatcher_label = Label(dispatcher_label_name)
        dispatcher = Switch(Variable(state_var), dispatcher_cases)

        func.body = new_body + [dispatcher_label, dispatcher] + case_bodies
        return func

    def collect_all_variables(self, stmts: List[ASTNode]):
        """Collect all variable names (declared, assigned, or used in expressions)."""
        vars = set()

        def walk(node):
            if isinstance(node, VariableDecl):
                vars.add(node.name)
            elif isinstance(node, Variable):
                vars.add(node.name)
            elif isinstance(node, Assignment):
                if isinstance(node.target, Variable):
                    vars.add(node.target.name)
                walk(node.value)
            elif isinstance(node, BinaryOp):
                walk(node.left)
                walk(node.right)
            elif isinstance(node, FuncCall):
                for arg in node.args:
                    walk(arg)
            elif isinstance(node, list):
                for s in node:
                    walk(s)
            elif isinstance(node, IfStmt):
                walk(node.condition)
                walk(node.then_branch)
                if node.else_branch:
                    walk(node.else_branch)
            elif isinstance(node, ForStmt):
                if node.init:
                    if isinstance(node.init, VariableDecl):
                        vars.add(node.init.name)
                    elif isinstance(node.init, Assignment):
                        if isinstance(node.init.target, Variable):
                            vars.add(node.init.target.name)
                    elif isinstance(node.init, ExpressionStmt):
                        if isinstance(node.init.expr, Assignment):
                            if isinstance(node.init.expr.target, Variable):
                                vars.add(node.init.expr.target.name)
                    walk(node.init)
                if node.cond:
                    walk(node.cond)
                if node.update:
                    if isinstance(node.update, Assignment):
                        if isinstance(node.update.target, Variable):
                            vars.add(node.update.target.name)
                    elif isinstance(node.update, ExpressionStmt):
                        if isinstance(node.update.expr, Assignment):
                            if isinstance(node.update.expr.target, Variable):
                                vars.add(node.update.expr.target.name)
                    walk(node.update)
                walk(node.body)
            elif isinstance(node, WhileStmt):
                walk(node.condition)
                walk(node.body)
            elif isinstance(node, Return):
                if node.value:
                    walk(node.value)
            elif isinstance(node, ExpressionStmt):
                if node.expr:
                    walk(node.expr)
            elif isinstance(node, Print):
                for arg in node.args:
                    walk(arg)
            elif isinstance(node, Scan):
                for arg in node.args:
                    if isinstance(arg, Variable):
                        walk(arg)
            elif hasattr(node, "__dict__"):
                for val in node.__dict__.values():
                    if isinstance(val, ASTNode):
                        walk(val)
                    elif isinstance(val, list):
                        for item in val:
                            if isinstance(item, ASTNode):
                                walk(item)

        for s in stmts:
            walk(s)
        return vars

    def collect_returned_variable_names(self, stmts: List[ASTNode]):
        """Track returned variables (used in return statements)."""
        names = set()

        def walk(node):
            if isinstance(node, Return) and isinstance(node.value, Variable):
                names.add(node.value.name)
            elif isinstance(node, list):
                for s in node:
                    walk(s)
            elif isinstance(node, IfStmt):
                walk(node.then_branch)
                if node.else_branch:
                    walk(node.else_branch)
            elif isinstance(node, ForStmt):
                walk(node.body)
            elif isinstance(node, WhileStmt):
                walk(node.body)
            elif isinstance(node, ExpressionStmt):
                if node.expr:
                    walk(node.expr)
            elif isinstance(node, Print):
                for arg in node.args:
                    walk(arg)
            elif isinstance(node, Scan):
                for arg in node.args:
                    if isinstance(arg, Variable):
                        walk(arg)

        for s in stmts:
            walk(s)
        return names
