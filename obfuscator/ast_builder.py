from obfuscator.parser.ObfuMiniCVisitor import ObfuMiniCVisitor
from obfuscator.parser.ObfuMiniCVisitor import ObfuMiniCVisitor
from obfuscator.ast import (
    Program, Function, Parameter, VariableDecl, ExpressionStmt, Return,
    IfStmt, WhileStmt, ForStmt, Print, Scan, Assignment, BinaryOp,
    UnaryOp, FuncCall, Variable, Literal
)

class ASTBuilder(ObfuMiniCVisitor):

    def visitCompilationUnit(self, ctx) :
        functions = []
        for child in ctx.children:
            result = self.visit(child)
            if result:
                functions.append(result)
        return Program(functions)

    def visitFuncDef(self, ctx):
        return_type = ctx.type_().getText()
        name = ctx.ID().getText()
        params = self.visit(ctx.paramList()) if ctx.paramList() else []
        body = self.visit(ctx.blockStmt())
        return Function(return_type, name, params, body)

    def visitParamList(self, ctx):
        return [self.visit(p) for p in ctx.param()]

    def visitParam(self, ctx):
        return Parameter(ctx.type_().getText(), ctx.ID().getText())

    def visitBlockStmt(self, ctx):
        stmts = []
        for child in ctx.children[1:-1]:  # strip { and }
            stmt = self.visit(child)
            if isinstance(stmt, list):
                stmts.extend(stmt)
            elif stmt:
                stmts.append(stmt)
        return stmts

    def visitVarDecl(self, ctx):
        var_type = ctx.type_().getText()
        decls = []
        for init in ctx.initList().init():
            name = init.ID().getText()
            expr = self.visit(init.expr()) if init.expr() else None
            decls.append(VariableDecl(var_type, name, expr))
        return decls

    def visitExprStmt(self, ctx):
        return ExpressionStmt(self.visit(ctx.expr())) if ctx.expr() else ExpressionStmt(None)

    def visitReturnStmt(self, ctx):
        return Return(self.visit(ctx.expr()) if ctx.expr() else None)

    def visitIfStmt(self, ctx):
        cond = self.visit(ctx.expr())
        then_stmt = self.visit(ctx.stmt(0))
        else_stmt = self.visit(ctx.stmt(1)) if ctx.ELSE() else None
        return IfStmt(cond, then_stmt, else_stmt)

    def visitLoopStmt(self, ctx):
        if ctx.WHILE():
            return WhileStmt(self.visit(ctx.expr(0)), self.visit(ctx.stmt()))
        else:
            return ForStmt(
                self.visit(ctx.expr(0)) if ctx.expr(0) else None,
                self.visit(ctx.expr(1)) if ctx.expr(1) else None,
                self.visit(ctx.expr(2)) if ctx.expr(2) else None,
                self.visit(ctx.stmt())
            )

    def visitIoStmt(self, ctx):
        if ctx.getChild(0).getText() == 'printf':
            fmt = ctx.STRING().getText().strip('"')
            args = [self.visit(e) for e in ctx.expr()]
            return Print(fmt, args)
        else:
            fmt = ctx.STRING().getText().strip('"')
            args = [id_tok.getText().replace('&', '') for id_tok in ctx.ID()]
            return Scan(fmt, args)

    def visitAssignExpr(self, ctx):
        if ctx.getChildCount() == 3:
            return Assignment(ctx.getChild(0).getText(), self.visit(ctx.assignExpr()))
        return self.visit(ctx.logicOrExpr())

    def visitLogicOrExpr(self, ctx):
        if len(ctx.children) == 1:
            return self.visit(ctx.logicAndExpr(0))
        left = self.visit(ctx.logicAndExpr(0))
        for i in range(1, len(ctx.logicAndExpr())):
            right = self.visit(ctx.logicAndExpr(i))
            left = BinaryOp("||", left, right)
        return left

    def visitLogicAndExpr(self, ctx):
        if len(ctx.children) == 1:
            return self.visit(ctx.equalityExpr(0))
        left = self.visit(ctx.equalityExpr(0))
        for i in range(1, len(ctx.equalityExpr())):
            right = self.visit(ctx.equalityExpr(i))
            left = BinaryOp("&&", left, right)
        return left

    def visitEqualityExpr(self, ctx):
        left = self.visit(ctx.relationalExpr(0))
        for i in range(1, len(ctx.relationalExpr())):
            op = ctx.getChild(2*i - 1).getText()
            right = self.visit(ctx.relationalExpr(i))
            left = BinaryOp(op, left, right)
        return left

    def visitRelationalExpr(self, ctx):
        left = self.visit(ctx.addExpr(0))
        for i in range(1, len(ctx.addExpr())):
            op = ctx.getChild(2*i - 1).getText()
            right = self.visit(ctx.addExpr(i))
            left = BinaryOp(op, left, right)
        return left

    def visitAddExpr(self, ctx):
        left = self.visit(ctx.mulExpr(0))
        for i in range(1, len(ctx.mulExpr())):
            op = ctx.getChild(2*i - 1).getText()
            right = self.visit(ctx.mulExpr(i))
            left = BinaryOp(op, left, right)
        return left

    def visitMulExpr(self, ctx):
        left = self.visit(ctx.unaryExpr(0))
        for i in range(1, len(ctx.unaryExpr())):
            op = ctx.getChild(2*i - 1).getText()
            right = self.visit(ctx.unaryExpr(i))
            left = BinaryOp(op, left, right)
        return left

    def visitUnaryExpr(self, ctx):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.unaryExpr()))
        return self.visit(ctx.primaryExpr())

    def visitPrimaryExpr(self, ctx):
        if ctx.ID() and ctx.expr():
            return FuncCall(ctx.ID().getText(), self.visit(ctx.argList()) if ctx.argList() else [])
        elif ctx.ID():
            return Variable(ctx.ID().getText())
        elif ctx.NUMBER():
            return Literal(int(ctx.NUMBER().getText()))
        elif ctx.BOOL():
            return Literal(ctx.BOOL().getText() == "true")
        elif ctx.CHAR():
            return Literal(ctx.CHAR().getText().strip("'"))
        elif ctx.STRING():
            return Literal(ctx.STRING().getText().strip('"'))
        elif ctx.expr():
            return self.visit(ctx.expr())
        else:
            return None

    def visitArgList(self, ctx):
        return [self.visit(e) for e in ctx.expr()]
