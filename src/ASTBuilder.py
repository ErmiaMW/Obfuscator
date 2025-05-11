from src.Grammar.MiniCVisitor import MiniCVisitor
from src.Grammar.MiniCParser import MiniCParser
from src import nodes

class ASTBuilder(MiniCVisitor):
    def visitProgram(self, ctx):
        decls = [self.visit(child) for child in ctx.children if child.getText() != '<EOF>']
        return nodes.ProgramNode(decls)

    def visitFunctionDecl(self, ctx):
        return_type = ctx.typeSpecifier().getText()
        name = ctx.IDENTIFIER().getText()
        params = self.visit(ctx.params()) if ctx.params() else []
        body = self.visit(ctx.compoundStmt())
        return nodes.FunctionDeclNode(return_type, name, params, body)

    def visitParams(self, ctx):
        return [self.visit(p) for p in ctx.param()]

    def visitParam(self, ctx):
        return nodes.ParamNode(ctx.typeSpecifier().getText(), ctx.IDENTIFIER().getText())

    def visitDeclaration(self, ctx):
        decls = []
        for initDecl in ctx.initDeclaratorList().initDeclarator():
            name = initDecl.IDENTIFIER().getText()
            init_expr = self.visit(initDecl.expression()) if initDecl.expression() else None
            decls.append(nodes.VarDeclNode(ctx.typeSpecifier().getText(), name, init_expr))
        return decls

    def visitCompoundStmt(self, ctx):
        stmts = []
        for child in ctx.children[1:-1]:  # skip { and }
            result = self.visit(child)
            if isinstance(result, list): stmts.extend(result)
            elif result: stmts.append(result)
        return nodes.CompoundStmtNode(stmts)

    def visitExpressionStmt(self, ctx):
        expr = self.visit(ctx.expression()) if ctx.expression() else None
        return nodes.ExpressionStmtNode(expr)

    def visitSelectionStmt(self, ctx):
        condition = self.visit(ctx.expression())
        then_stmt = self.visit(ctx.statement(0))
        else_stmt = self.visit(ctx.statement(1)) if ctx.ELSE() else None
        return nodes.IfNode(condition, then_stmt, else_stmt)

    def visitIterationStmt(self, ctx):
        if ctx.WHILE():
            condition = self.visit(ctx.expression())
            body = self.visit(ctx.statement(0))
            return nodes.WhileNode(condition, body)
        else:
            init = self.visit(ctx.expression(0)) if ctx.expression(0) else None
            cond = self.visit(ctx.expression(1)) if ctx.expression(1) else None
            post = self.visit(ctx.expression(2)) if ctx.expression(2) else None
            body = self.visit(ctx.statement())
            return nodes.ForNode(init, cond, post, body)

    def visitReturnStmt(self, ctx):
        expr = self.visit(ctx.expression()) if ctx.expression() else None
        return nodes.ReturnNode(expr)

    def visitIoStmt(self, ctx):
        # kind = 'printf' if ctx.PRINTF() else 'scanf'
        kind = ctx.getChild(0).getText()
        fmt_str = ctx.STRING().getText()
        args = [self.visit(e) for e in ctx.expression()] if ctx.expression() else []
        return nodes.IONode(kind, fmt_str, args)

    def visitAssignmentExpr(self, ctx):
        if ctx.getChildCount() == 3 and ctx.getChild(1).getText() == '=':
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            return nodes.AssignmentNode(left, right)
        return self.visitChildren(ctx)

    def visitLogicalOrExpr(self, ctx):
        return self._binary(ctx, nodes.BinaryOpNode, '||')

    def visitLogicalAndExpr(self, ctx):
        return self._binary(ctx, nodes.BinaryOpNode, '&&')

    def visitEqualityExpr(self, ctx):
        return self._binary(ctx, nodes.BinaryOpNode, ['==', '!='])

    def visitRelationalExpr(self, ctx):
        return self._binary(ctx, nodes.BinaryOpNode, ['<', '<=', '>', '>='])

    def visitAdditiveExpr(self, ctx):
        return self._binary(ctx, nodes.BinaryOpNode, ['+', '-'])

    def visitMultiplicativeExpr(self, ctx):
        return self._binary(ctx, nodes.BinaryOpNode, ['*', '/', '%'])

    def visitUnaryExpr(self, ctx):
        if ctx.getChildCount() == 2:
            return nodes.UnaryOpNode(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        return self.visit(ctx.getChild(0))

    def visitPrimaryExpr(self, ctx):
        if ctx.IDENTIFIER():
            if ctx.getChildCount() > 1:  # function call
                name = ctx.IDENTIFIER().getText()
                args = self.visit(ctx.argumentList()) if ctx.argumentList() else []
                return nodes.FunctionCallNode(name, args)
            return nodes.IdentifierNode(ctx.IDENTIFIER().getText())
        elif ctx.NUMBER():
            return nodes.LiteralNode(int(ctx.NUMBER().getText()))
        elif ctx.CHAR():
            return nodes.LiteralNode(ctx.CHAR().getText())
        elif ctx.BOOL():
            return nodes.LiteralNode(ctx.BOOL().getText() == "true")
        elif ctx.STRING():
            return nodes.LiteralNode(ctx.STRING().getText())
        elif ctx.expression():
            return self.visit(ctx.expression())
        return None

    def visitArgumentList(self, ctx):
        return [self.visit(e) for e in ctx.expression()]

    def _binary(self, ctx, node_type, ops):
        if isinstance(ops, str): ops = [ops]
        if ctx.getChildCount() == 3 and ctx.getChild(1).getText() in ops:
            left = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))
            return node_type(op, left, right)
        return self.visit(ctx.getChild(0))
