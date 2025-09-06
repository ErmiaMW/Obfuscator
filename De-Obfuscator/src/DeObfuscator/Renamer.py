from antlr4 import *
from src.Grammar.MiniCLexer import MiniCLexer
from src.Grammar.MiniCParser import MiniCParser
from src.Grammar.MiniCVisitor import MiniCVisitor
from antlr4.TokenStreamRewriter import TokenStreamRewriter


class SemanticRenameVisitor(MiniCVisitor):
    def __init__(self, token_stream):
        self.rewriter = TokenStreamRewriter(token_stream)
        self.token_stream = token_stream
        self.name_map = {}
        self.func_count = 0
        self.var_count = 0
        self.skip_names = {'main'}

    def _generate_func_name(self, original):
        # Try to guess based on usage
        if "print" in original.lower():
            return "printHelper"
        self.func_count += 1
        return f"func{self.func_count}"

    def _generate_var_name(self, ctx, original):
        # Heuristic 1: loop counter
        parent = ctx.parentCtx
        if parent and parent.__class__.__name__ in ["ForStmt", "WhileStmt"]:
            return "i" if "i" not in self.name_map.values() else "j"

        # Heuristic 2: arithmetic operation
        if ctx.parentCtx and ctx.parentCtx.__class__.__name__ == "AssignmentExpr":
            expr_text = ctx.parentCtx.getText()
            if "+" in expr_text:
                return "sum"
            elif "-" in expr_text:
                return "diff"
            elif "*" in expr_text:
                return "product"

        # Default naming
        basic_names = ["x", "y", "z", "a", "b", "c"]
        if self.var_count < len(basic_names):
            name = basic_names[self.var_count]
        else:
            name = f"var{self.var_count}"
        self.var_count += 1
        return name

    def _rename(self, original, ctx, is_func=False):
        if original in self.skip_names:
            return original
        if original not in self.name_map:
            if is_func:
                self.name_map[original] = self._generate_func_name(original)
            else:
                self.name_map[original] = self._generate_var_name(ctx, original)
        return self.name_map[original]

    # --- Visitor Methods ---

    def visitFunctionDecl(self, ctx):
        name_token = ctx.IDENTIFIER().getSymbol()
        if name_token.text not in self.skip_names:
            new_name = self._rename(name_token.text, ctx, is_func=True)
            self.rewriter.replaceSingleToken(name_token, new_name)
        self.visitChildren(ctx)
        return None

    def visitParam(self, ctx):
        name_token = ctx.IDENTIFIER().getSymbol()
        new_name = self._rename(name_token.text, ctx, is_func=False)
        self.rewriter.replaceSingleToken(name_token, new_name)
        return None

    def visitInitDeclarator(self, ctx):
        name_token = ctx.IDENTIFIER().getSymbol()
        new_name = self._rename(name_token.text, ctx, is_func=False)
        self.rewriter.replaceSingleToken(name_token, new_name)
        self.visitChildren(ctx)
        return None

    def visitPrimaryExpr(self, ctx):
        if ctx.IDENTIFIER() and ctx.getChildCount() == 1:
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


def renamer(input_path, output_path):
    input_stream = FileStream(input_path, encoding="utf-8")
    lexer = MiniCLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiniCParser(tokens)
    tree = parser.program()

    visitor = SemanticRenameVisitor(tokens)
    visitor.visit(tree)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(visitor.rewriter.getDefaultText())
