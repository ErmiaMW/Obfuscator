from antlr4 import *
from src.Grammar.MiniCLexer import MiniCLexer
from src.Grammar.MiniCParser import MiniCParser
from src.Grammar.MiniCVisitor import MiniCVisitor
from antlr4.TokenStreamRewriter import TokenStreamRewriter
import re

class FunctionInliningVisitor(MiniCVisitor):
    def __init__(self, token_stream):
        self.rewriter = TokenStreamRewriter(token_stream)
        self.token_stream = token_stream
        self.functions = {} 

    def visitFunctionDef(self, ctx):
        func_name = ctx.IDENTIFIER().getText()
        if func_name == "main":
            return self.visitChildren(ctx)

        params = [p.IDENTIFIER().getText() for p in ctx.declarator().parameterList().parameterDeclaration()] if ctx.declarator().parameterList() else []
        body = ctx.compoundStmt().getText()

        match = re.search(r'return\s+([^;]+);', body)
        if match:
            return_expr = match.group(1)
            self.functions[func_name] = (params, return_expr)
            self.rewriter.delete(ctx.start.tokenIndex, ctx.stop.tokenIndex)
        return None

    def visitPostfixExpr(self, ctx):
        if ctx.getChildCount() >= 3 and ctx.getChild(1).getText() == '(':
            func_name = ctx.getChild(0).getText()
            if func_name in self.functions:
                param_names, return_expr = self.functions[func_name]
                arg_texts = [ctx.getChild(i).getText() for i in range(2, ctx.getChildCount() - 1, 2)]

                if len(param_names) != len(arg_texts):
                    return self.visitChildren(ctx)

                inlined = return_expr
                for p, a in zip(param_names, arg_texts):
                    inlined = re.sub(r'\b' + re.escape(p) + r'\b', a, inlined)

                self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, f"({inlined})")

        return self.visitChildren(ctx)


def function_inlining(input_path, output_path):
    input_stream = FileStream(input_path, encoding="utf-8")
    lexer = MiniCLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiniCParser(tokens)
    tree = parser.program()

    visitor = FunctionInliningVisitor(tokens)
    visitor.visit(tree)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(visitor.rewriter.getDefaultText())
