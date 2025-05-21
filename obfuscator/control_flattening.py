from obfuscator.ast import *
from itertools import count

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

        state_decl = VariableDecl("int", state_var, Literal(0))
        new_body = [state_decl]

        dispatcher_cases = []
        case_bodies = []

        for i, stmt in enumerate(func.body):
            case_label_name = f"{prefix}_case_{i}"
            label = Label(case_label_name)
            case_body = [stmt]

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
