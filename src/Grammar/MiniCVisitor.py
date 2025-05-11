# Generated from Grammar/MiniC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniCParser import MiniCParser
else:
    from MiniCParser import MiniCParser

# This class defines a complete generic visitor for a parse tree produced by MiniCParser.

class MiniCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniCParser#program.
    def visitProgram(self, ctx:MiniCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#functionDecl.
    def visitFunctionDecl(self, ctx:MiniCParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#params.
    def visitParams(self, ctx:MiniCParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#param.
    def visitParam(self, ctx:MiniCParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#declaration.
    def visitDeclaration(self, ctx:MiniCParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#initDeclaratorList.
    def visitInitDeclaratorList(self, ctx:MiniCParser.InitDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#initDeclarator.
    def visitInitDeclarator(self, ctx:MiniCParser.InitDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:MiniCParser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#compoundStmt.
    def visitCompoundStmt(self, ctx:MiniCParser.CompoundStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#statement.
    def visitStatement(self, ctx:MiniCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#expressionStmt.
    def visitExpressionStmt(self, ctx:MiniCParser.ExpressionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#selectionStmt.
    def visitSelectionStmt(self, ctx:MiniCParser.SelectionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#iterationStmt.
    def visitIterationStmt(self, ctx:MiniCParser.IterationStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#returnStmt.
    def visitReturnStmt(self, ctx:MiniCParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#ioStmt.
    def visitIoStmt(self, ctx:MiniCParser.IoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#expression.
    def visitExpression(self, ctx:MiniCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#assignmentExpr.
    def visitAssignmentExpr(self, ctx:MiniCParser.AssignmentExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#logicalOrExpr.
    def visitLogicalOrExpr(self, ctx:MiniCParser.LogicalOrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#logicalAndExpr.
    def visitLogicalAndExpr(self, ctx:MiniCParser.LogicalAndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#equalityExpr.
    def visitEqualityExpr(self, ctx:MiniCParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#relationalExpr.
    def visitRelationalExpr(self, ctx:MiniCParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:MiniCParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:MiniCParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#unaryExpr.
    def visitUnaryExpr(self, ctx:MiniCParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:MiniCParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#argumentList.
    def visitArgumentList(self, ctx:MiniCParser.ArgumentListContext):
        return self.visitChildren(ctx)



del MiniCParser