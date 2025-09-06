import re
from antlr4 import *
from src.Grammar.MiniCLexer import MiniCLexer
from src.Grammar.MiniCParser import MiniCParser
from src.Grammar.MiniCVisitor import MiniCVisitor
from antlr4.TokenStreamRewriter import TokenStreamRewriter


class EquivalentExpressionDeobfuscator(MiniCVisitor):
    def __init__(self, token_stream: CommonTokenStream):
        self.rewriter = TokenStreamRewriter(token_stream)
        self.token_stream = token_stream


    @staticmethod
    def _strip_outer_parens(s: str) -> str:
        s = s.strip()
        if len(s) >= 2 and s[0] == '(' and s[-1] == ')':
            depth = 0
            for i, ch in enumerate(s):
                if ch == '(':
                    depth += 1
                elif ch == ')':
                    depth -= 1
                    if depth == 0 and i != len(s) - 1:
                        return s
            return s[1:-1].strip()
        return s

    @staticmethod
    def _split_top_level(expr: str, ops=('\!=', '==')):
        expr = expr.strip()
        depth = 0
        i = 0
        while i < len(expr):
            ch = expr[i]
            if ch == '(':
                depth += 1
                i += 1
                continue
            if ch == ')':
                depth -= 1
                i += 1
                continue
            if depth == 0:
                if expr.startswith('==', i):
                    return expr[:i].strip(), '==', expr[i+2:].strip()
                if expr.startswith('!=', i):
                    return expr[:i].strip(), '!=', expr[i+2:].strip()
            i += 1
        return None, None, None


    def visitAdditiveExpr(self, ctx: MiniCParser.AdditiveExprContext):
        if ctx.getChildCount() == 3:
            left_text = self.token_stream.getText(ctx.getChild(0).start.tokenIndex,
                                                  ctx.getChild(0).stop.tokenIndex)
            op_text = ctx.getChild(1).getText()
            right_text = self.token_stream.getText(ctx.getChild(2).start.tokenIndex,
                                                   ctx.getChild(2).stop.tokenIndex)

            right_compact = ''.join(right_text.split())  # remove spaces for pattern match
            if right_compact.startswith('(-') and right_compact.endswith(')'):
                inner = right_text.strip()
                inner = self._strip_outer_parens(inner)
                if inner.startswith('-'):
                    inner = inner[1:].strip()
                inner = self._strip_outer_parens(inner)

                if op_text == '-':
                    new_expr = f"{left_text} + {inner}"
                    self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, new_expr)
                elif op_text == '+':
                    new_expr = f"{left_text} - {inner}"
                    self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, new_expr)

        return self.visitChildren(ctx)

    def visitUnaryExpr(self, ctx: MiniCParser.UnaryExprContext):

        if ctx.getChildCount() == 2 and ctx.getChild(0).getText() == '!':
            operand = ctx.getChild(1)
            op_start = operand.start.tokenIndex
            op_stop = operand.stop.tokenIndex
            operand_text = self.token_stream.getText(op_start, op_stop).strip()

            inner = self._strip_outer_parens(operand_text)

            left, op, right = self._split_top_level(inner, ops=('!=', '=='))
            if op in ('==', '!=') and left is not None and right is not None:
                flipped = '!=' if op == '==' else '=='
                simplified = f"{left} {flipped} {right}"
                self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, simplified)

        return self.visitChildren(ctx)


def expression_simplifier(input_path: str, output_path: str):
    input_stream = FileStream(input_path, encoding="utf-8")
    lexer = MiniCLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiniCParser(tokens)
    tree = parser.program()

    deob = EquivalentExpressionDeobfuscator(tokens)
    deob.visit(tree)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(deob.rewriter.getDefaultText())
