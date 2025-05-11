import random
from antlr4 import *
from src.Grammar.MiniCLexer import MiniCLexer
from src.Grammar.MiniCParser import MiniCParser
from src.Grammar.MiniCVisitor import MiniCVisitor
from antlr4.TokenStreamRewriter import TokenStreamRewriter

class EquivalentExprVisitor(MiniCVisitor):
    def __init__(self, token_stream):
        self.rewriter = TokenStreamRewriter(token_stream)

    def _replace_expr(self, ctx, new_expr):
        self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, new_expr)

    def visitAssignmentExpr(self, ctx):
        if ctx.getChildCount() == 3:
            left = ctx.getChild(0).getText()
            op = ctx.getChild(1).getText()
            right = ctx.getChild(2).getText()

            try:
                val = int(right)
                if op == "+":
                    new_expr = f"{left} = {ctx.getChild(0).getText()} - ({-val});"
                    self._replace_expr(ctx, new_expr)
                elif op == "-":
                    new_expr = f"{left} = {ctx.getChild(0).getText()} + ({-val});"
                    self._replace_expr(ctx, new_expr)
                elif op == "*":
                    if val in [2, 4, 8]:
                        shift = {2:1, 4:2, 8:3}[val]
                        new_expr = f"{left} = {ctx.getChild(0).getText()} << {shift};"
                        self._replace_expr(ctx, new_expr)
                elif op == "/":
                    if val in [2, 4, 8]:
                        shift = {2:1, 4:2, 8:3}[val]
                        new_expr = f"{left} = {ctx.getChild(0).getText()} >> {shift};"
                        self._replace_expr(ctx, new_expr)
            except:
                pass

        return self.visitChildren(ctx)

    def visitEqualityExpr(self, ctx):
        if ctx.getChildCount() == 3:
            left = ctx.getChild(0).getText()
            op = ctx.getChild(1).getText()
            right = ctx.getChild(2).getText()
            if op == "==":
                new_expr = f"!({left} != {right})"
                self._replace_expr(ctx, new_expr)
            elif op == "!=":
                new_expr = f"!({left} == {right})"
                self._replace_expr(ctx, new_expr)

        return self.visitChildren(ctx)

    def visitRelationalExpr(self, ctx):
        if ctx.getChildCount() == 3:
            left = ctx.getChild(0).getText()
            op = ctx.getChild(1).getText()
            right = ctx.getChild(2).getText()
            inverse_map = {
                ">": f"!({left} <= {right})",
                "<": f"!({left} >= {right})",
                ">=": f"!({left} < {right})",
                "<=": f"!({left} > {right})"
            }
            if op in inverse_map:
                self._replace_expr(ctx, inverse_map[op])

        return self.visitChildren(ctx)

    def visitLogicalOrExpr(self, ctx):
        if ctx.getChildCount() == 3 and ctx.getChild(1).getText() == '||':
            expr = ctx.getText()
            new_expr = f"!!({expr})"
            self._replace_expr(ctx, new_expr)
        return self.visitChildren(ctx)

    def visitLogicalAndExpr(self, ctx):
        if ctx.getChildCount() == 3 and ctx.getChild(1).getText() == '&&':
            expr = ctx.getText()
            new_expr = f"!!({expr})"
            self._replace_expr(ctx, new_expr)
        return self.visitChildren(ctx)


def equaivalent_expression(input_path, output_path):
    input_stream = FileStream(input_path, encoding="utf-8")
    lexer = MiniCLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiniCParser(tokens)
    tree = parser.program()

    visitor = EquivalentExprVisitor(tokens)
    visitor.visit(tree)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(visitor.rewriter.getDefaultText())
