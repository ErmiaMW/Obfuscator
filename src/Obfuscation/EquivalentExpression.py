from antlr4 import *
from src.Grammar.MiniCLexer import MiniCLexer
from src.Grammar.MiniCParser import MiniCParser
from src.Grammar.MiniCVisitor import MiniCVisitor
from antlr4.TokenStreamRewriter import TokenStreamRewriter

class ExpressionTransformer(MiniCVisitor):
    def __init__(self, token_stream):
        self.rewriter = TokenStreamRewriter(token_stream)
        self.token_stream = token_stream

    def visitAdditiveExpr(self, ctx):
        if ctx.getChildCount() == 3:
            left = ctx.getChild(0).getText()
            op = ctx.getChild(1).getText()
            right = ctx.getChild(2).getText()

            if op == '+':
                new_expr = f"{left} - (-{right})"
                self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, new_expr)
            elif op == '-':
                new_expr = f"{left} + (-{right})"
                self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, new_expr)

        return self.visitChildren(ctx)

    def visitEqualityExpr(self, ctx):
        if ctx.getChildCount() == 3:
            left = ctx.getChild(0).getText()
            op = ctx.getChild(1).getText()
            right = ctx.getChild(2).getText()

            if op == '==':
                new_expr = f"!({left} != {right})"
                self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, new_expr)
            elif op == '!=':
                new_expr = f"!({left} == {right})"
                self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, new_expr)

        return self.visitChildren(ctx)


def equaivalent_expression(input_path, output_path):
    input_stream = FileStream(input_path, encoding="utf-8")
    lexer = MiniCLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiniCParser(tokens)
    tree = parser.program()

    transformer = ExpressionTransformer(tokens)
    transformer.visit(tree)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(transformer.rewriter.getDefaultText())
