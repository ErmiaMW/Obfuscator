# Generated from MiniC.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniCParser import MiniCParser
else:
    from MiniCParser import MiniCParser

# This class defines a complete listener for a parse tree produced by MiniCParser.
class MiniCListener(ParseTreeListener):

    # Enter a parse tree produced by MiniCParser#program.
    def enterProgram(self, ctx:MiniCParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniCParser#program.
    def exitProgram(self, ctx:MiniCParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniCParser#functionDecl.
    def enterFunctionDecl(self, ctx:MiniCParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by MiniCParser#functionDecl.
    def exitFunctionDecl(self, ctx:MiniCParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by MiniCParser#params.
    def enterParams(self, ctx:MiniCParser.ParamsContext):
        pass

    # Exit a parse tree produced by MiniCParser#params.
    def exitParams(self, ctx:MiniCParser.ParamsContext):
        pass


    # Enter a parse tree produced by MiniCParser#param.
    def enterParam(self, ctx:MiniCParser.ParamContext):
        pass

    # Exit a parse tree produced by MiniCParser#param.
    def exitParam(self, ctx:MiniCParser.ParamContext):
        pass


    # Enter a parse tree produced by MiniCParser#declaration.
    def enterDeclaration(self, ctx:MiniCParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MiniCParser#declaration.
    def exitDeclaration(self, ctx:MiniCParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MiniCParser#initDeclaratorList.
    def enterInitDeclaratorList(self, ctx:MiniCParser.InitDeclaratorListContext):
        pass

    # Exit a parse tree produced by MiniCParser#initDeclaratorList.
    def exitInitDeclaratorList(self, ctx:MiniCParser.InitDeclaratorListContext):
        pass


    # Enter a parse tree produced by MiniCParser#initDeclarator.
    def enterInitDeclarator(self, ctx:MiniCParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by MiniCParser#initDeclarator.
    def exitInitDeclarator(self, ctx:MiniCParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by MiniCParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:MiniCParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by MiniCParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:MiniCParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by MiniCParser#compoundStmt.
    def enterCompoundStmt(self, ctx:MiniCParser.CompoundStmtContext):
        pass

    # Exit a parse tree produced by MiniCParser#compoundStmt.
    def exitCompoundStmt(self, ctx:MiniCParser.CompoundStmtContext):
        pass


    # Enter a parse tree produced by MiniCParser#statement.
    def enterStatement(self, ctx:MiniCParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniCParser#statement.
    def exitStatement(self, ctx:MiniCParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniCParser#expressionStmt.
    def enterExpressionStmt(self, ctx:MiniCParser.ExpressionStmtContext):
        pass

    # Exit a parse tree produced by MiniCParser#expressionStmt.
    def exitExpressionStmt(self, ctx:MiniCParser.ExpressionStmtContext):
        pass


    # Enter a parse tree produced by MiniCParser#selectionStmt.
    def enterSelectionStmt(self, ctx:MiniCParser.SelectionStmtContext):
        pass

    # Exit a parse tree produced by MiniCParser#selectionStmt.
    def exitSelectionStmt(self, ctx:MiniCParser.SelectionStmtContext):
        pass


    # Enter a parse tree produced by MiniCParser#iterationStmt.
    def enterIterationStmt(self, ctx:MiniCParser.IterationStmtContext):
        pass

    # Exit a parse tree produced by MiniCParser#iterationStmt.
    def exitIterationStmt(self, ctx:MiniCParser.IterationStmtContext):
        pass


    # Enter a parse tree produced by MiniCParser#returnStmt.
    def enterReturnStmt(self, ctx:MiniCParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by MiniCParser#returnStmt.
    def exitReturnStmt(self, ctx:MiniCParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by MiniCParser#ioStmt.
    def enterIoStmt(self, ctx:MiniCParser.IoStmtContext):
        pass

    # Exit a parse tree produced by MiniCParser#ioStmt.
    def exitIoStmt(self, ctx:MiniCParser.IoStmtContext):
        pass


    # Enter a parse tree produced by MiniCParser#expression.
    def enterExpression(self, ctx:MiniCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#expression.
    def exitExpression(self, ctx:MiniCParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#assignmentExpr.
    def enterAssignmentExpr(self, ctx:MiniCParser.AssignmentExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#assignmentExpr.
    def exitAssignmentExpr(self, ctx:MiniCParser.AssignmentExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#logicalOrExpr.
    def enterLogicalOrExpr(self, ctx:MiniCParser.LogicalOrExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#logicalOrExpr.
    def exitLogicalOrExpr(self, ctx:MiniCParser.LogicalOrExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#logicalAndExpr.
    def enterLogicalAndExpr(self, ctx:MiniCParser.LogicalAndExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#logicalAndExpr.
    def exitLogicalAndExpr(self, ctx:MiniCParser.LogicalAndExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#equalityExpr.
    def enterEqualityExpr(self, ctx:MiniCParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#equalityExpr.
    def exitEqualityExpr(self, ctx:MiniCParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#relationalExpr.
    def enterRelationalExpr(self, ctx:MiniCParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#relationalExpr.
    def exitRelationalExpr(self, ctx:MiniCParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:MiniCParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:MiniCParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#multiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:MiniCParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#multiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:MiniCParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#unaryExpr.
    def enterUnaryExpr(self, ctx:MiniCParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#unaryExpr.
    def exitUnaryExpr(self, ctx:MiniCParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:MiniCParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:MiniCParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#argumentList.
    def enterArgumentList(self, ctx:MiniCParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by MiniCParser#argumentList.
    def exitArgumentList(self, ctx:MiniCParser.ArgumentListContext):
        pass



del MiniCParser