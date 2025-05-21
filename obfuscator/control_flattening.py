from obfuscator.ast import *

class ControlFlowFlattener:
    def flatten(self, program: Program):
        for i, func in enumerate(program.functions):
            program.functions[i] = self._flatten_function(func)

    def _flatten_function(self, func: Function):
        if not func.body:
            return func

        state_decl = VariableDecl("int", "_state", Literal(0))
        new_body = [state_decl]

        dispatcher_cases = []
        case_bodies = []

        for i, stmt in enumerate(func.body):
            label = Label(f"case_{i}")
            case_body = [stmt]

            if not isinstance(stmt, Return):
                case_body.append(Assignment(Variable("_state"), Literal(i + 1)))
                case_body.append(Goto("dispatcher"))

            dispatcher_cases.append(SwitchCase(Literal(i), label, None))  # فقط label در switch
            case_bodies.append(Block([label] + case_body))  # بدنه هر case جداست

        end_label = Label("case_end")
        dispatcher_cases.append(SwitchCase(Literal(len(func.body)), end_label, None))
        case_bodies.append(Block([end_label, Return(Literal(0))]))

        dispatcher_label = Label("dispatcher")
        dispatcher = Switch(Variable("_state"), dispatcher_cases)

        # حالا همه را کنار هم می‌گذاریم
        func.body = new_body + [dispatcher_label, dispatcher] + case_bodies

        return func