import copy
from antlr4 import *
from src.Grammar.MiniCLexer import MiniCLexer
from src.Grammar.MiniCParser import MiniCParser
from src.Grammar.MiniCVisitor import MiniCVisitor
from antlr4.TokenStreamRewriter import TokenStreamRewriter

class FunctionInliner(MiniCVisitor):
    def __init__(self, token_stream):
        self.rewriter = TokenStreamRewriter(token_stream)
        self.token_stream = token_stream
        self.inlineable_funcs = {}

    def visitFunctionDecl(self, ctx):
        name = ctx.IDENTIFIER().getText()
        if name == "main":
            return self.visitChildren(ctx)

        params = ctx.params()
        compound = ctx.compoundStmt()
        stmts = compound.statement()

        if len(stmts) == 1 and stmts[0].returnStmt():
            return_expr = self.token_stream.getText(
                stmts[0].returnStmt().expression().start.tokenIndex,
                stmts[0].returnStmt().expression().stop.tokenIndex,
            )

            param_names = []
            if params:
                for param in params.param():
                    param_names.append(param.IDENTIFIER().getText())

            self.inlineable_funcs[name] = {
                "params": param_names,
                "body": return_expr,
            }

        return self.visitChildren(ctx)

    def visitPrimaryExpr(self, ctx):
        if ctx.getChildCount() >= 3 and ctx.getChild(1).getText() == '(':
            func_name = ctx.IDENTIFIER().getText()

            if func_name in self.inlineable_funcs:
                func_info = self.inlineable_funcs[func_name]
                body = func_info["body"]
                param_names = func_info["params"]

                args = []
                if ctx.argumentList():
                    for expr in ctx.argumentList().expression():
                        text = self.token_stream.getText(expr.start.tokenIndex, expr.stop.tokenIndex)
                        args.append(text)

                inline_expr = body
                for p, a in zip(param_names, args):
                    inline_expr = inline_expr.replace(p, f"({a})")

                self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, inline_expr)

        return self.visitChildren(ctx)


def function_inlining(input_path, output_path):
    input_stream = FileStream(input_path, encoding="utf-8")
    lexer = MiniCLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiniCParser(tokens)
    tree = parser.program()

    inliner = FunctionInliner(tokens)
    inliner.visit(tree)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(inliner.rewriter.getDefaultText())
