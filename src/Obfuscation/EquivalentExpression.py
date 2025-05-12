from antlr4 import *
from src.Grammar.MiniCLexer import MiniCLexer
from src.Grammar.MiniCParser import MiniCParser
from src.Grammar.MiniCVisitor import MiniCVisitor
from antlr4.TokenStreamRewriter import TokenStreamRewriter

class EquivalentExpressionVisitor(MiniCVisitor):
    def __init__(self, token_stream):
        self.rewriter = TokenStreamRewriter(token_stream)

    def visitAdditiveExpr(self, ctx):
        if ctx.getChildCount() == 3:
            left = ctx.getChild(0).getText()
            op = ctx.getChild(1).getText()
            right = ctx.getChild(2).getText()

            # فقط اگر operand عددی ساده باشد
            try:
                val = int(right)
                if op == '+':
                    expr = f"{left} - (-{val})"
                    self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, expr)
                elif op == '-':
                    expr = f"{left} + (-{val})"
                    self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, expr)
            except:
                pass

        return self.visitChildren(ctx)

    def visitEqualityExpr(self, ctx):
        if ctx.getChildCount() == 3:
            left = ctx.getChild(0).getText()
            op = ctx.getChild(1).getText()
            right = ctx.getChild(2).getText()

            if op == "==":
                expr = f"!({left} != {right})"
                self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, expr)
            elif op == "!=":
                expr = f"!({left} == {right})"
                self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, expr)

        return self.visitChildren(ctx)

    def visitRelationalExpr(self, ctx):
        if ctx.getChildCount() == 3:
            left = ctx.getChild(0).getText()
            op = ctx.getChild(1).getText()
            right = ctx.getChild(2).getText()

            if op == "<":
                expr = f"!({left} >= {right})"
                self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, expr)
            elif op == ">":
                expr = f"!({left} <= {right})"
                self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, expr)
            elif op == "<=":
                expr = f"!({left} > {right})"
                self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, expr)
            elif op == ">=":
                expr = f"!({left} < {right})"
                self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, expr)

        return self.visitChildren(ctx)

    def visitLogicalAndExpr(self, ctx):
        if ctx.getChildCount() == 3 and ctx.getChild(1).getText() == "&&":
            text = ctx.getText()
            expr = f"!!({text})"
            self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, expr)
        return self.visitChildren(ctx)

    def visitLogicalOrExpr(self, ctx):
        if ctx.getChildCount() == 3 and ctx.getChild(1).getText() == "||":
            text = ctx.getText()
            expr = f"!!({text})"
            self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, expr)
        return self.visitChildren(ctx)


def equaivalent_expression(input_path, output_path):
    input_stream = FileStream(input_path, encoding="utf-8")
    lexer = MiniCLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiniCParser(tokens)
    tree = parser.program()

    visitor = EquivalentExpressionVisitor(tokens)
    visitor.visit(tree)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(visitor.rewriter.getDefaultText())
