from antlr4 import *
from src.Grammar.MiniCLexer import MiniCLexer
from src.Grammar.MiniCParser import MiniCParser
from src.Grammar.MiniCVisitor import MiniCVisitor
from antlr4.TokenStreamRewriter import TokenStreamRewriter
import random
import string
class RenameVisitor(MiniCVisitor):
    def __init__(self, token_stream):
        self.rewriter = TokenStreamRewriter(token_stream)
        self.token_stream = token_stream
        self.name_map = {}
        self.used_names = set()

    def _generate_name(self):
        chars = string.ascii_letters + string.digits + '_'  # a-z, A-Z, 0-9, _
        while True:
            length = random.randint(3, 10)
            name = ''.join(random.choices(chars, k=length))
            if name not in self.used_names and not name[0].isdigit():  # avoid starting with a digit
                self.used_names.add(name)
                return name

    def _rename(self, original):
        if original not in self.name_map:
            self.name_map[original] = self._generate_name()
        return self.name_map[original]

    def visitFunctionDecl(self, ctx):
        name_token = ctx.IDENTIFIER().getSymbol()
        new_name = self._rename(name_token.text)
        self.rewriter.replaceSingleToken(name_token, new_name)
        self.visitChildren(ctx)
        return None

    def visitParam(self, ctx):
        name_token = ctx.IDENTIFIER().getSymbol()
        new_name = self._rename(name_token.text)
        self.rewriter.replaceSingleToken(name_token, new_name)
        return None

    def visitInitDeclarator(self, ctx):
        name_token = ctx.IDENTIFIER().getSymbol()
        new_name = self._rename(name_token.text)
        self.rewriter.replaceSingleToken(name_token, new_name)
        self.visitChildren(ctx)
        return None

    def visitPrimaryExpr(self, ctx):
        if ctx.IDENTIFIER() and ctx.getChildCount() == 1:  # only if it's not a function call
            original = ctx.IDENTIFIER().getText()
            if original in self.name_map:
                self.rewriter.replaceSingleToken(ctx.IDENTIFIER().getSymbol(), self.name_map[original])
        return self.visitChildren(ctx)

    def visitAssignmentExpr(self, ctx):
        if ctx.getChildCount() >= 3:
            left = ctx.getChild(0)
            if hasattr(left, "getSymbol"):
                name_token = left.getSymbol()
                if name_token.text in self.name_map:
                    self.rewriter.replaceSingleToken(name_token, self.name_map[name_token.text])
        return self.visitChildren(ctx)


def rename_variables_and_functions(input_path, output_path):
    input_stream = FileStream(input_path, encoding="utf-8")
    lexer = MiniCLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiniCParser(tokens)
    tree = parser.program()

    visitor = RenameVisitor(tokens)
    visitor.visit(tree)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(visitor.rewriter.getDefaultText())
