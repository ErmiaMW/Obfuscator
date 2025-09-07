from antlr4 import *
from src.Grammar.MiniCLexer import MiniCLexer
from src.Grammar.MiniCParser import MiniCParser
from src.Grammar.MiniCVisitor import MiniCVisitor
from antlr4.TokenStreamRewriter import TokenStreamRewriter


class SemanticRenameVisitor(MiniCVisitor):
    def __init__(self, token_stream):
        self.rewriter = TokenStreamRewriter(token_stream)
        self.token_stream = token_stream
        self.name_map = {}           # original -> new name
        self.func_count = 0
        self.var_count = 0
        # do not rename these (common entry points / std functions)
        self.skip_names = {'main', 'printf', 'scanf', 'puts', 'putchar', 'strlen', 'malloc', 'free', 'NULL'}

    def _generate_func_name(self, original):
        if "print" in original.lower():
            return "printHelper"
        self.func_count += 1
        return f"func{self.func_count}"

    def _generate_var_name(self, ctx, original):
        # simple heuristics: common names for first few variables
        basic_names = ["x", "y", "z", "a", "b", "c"]
        if self.var_count < len(basic_names):
            name = basic_names[self.var_count]
        else:
            name = f"var{self.var_count}"
        self.var_count += 1
        return name

    def _rename(self, original, ctx=None, is_func=False):
        if original in self.skip_names:
            return original
        if original not in self.name_map:
            if is_func:
                self.name_map[original] = self._generate_func_name(original)
            else:
                self.name_map[original] = self._generate_var_name(ctx, original)
        return self.name_map[original]

    # --- Visitor callbacks to collect mappings and replace declaration tokens ---
    def visitFunctionDecl(self, ctx):
        # grammar: functionDecl ... IDENTIFIER ...
        if hasattr(ctx, "IDENTIFIER") and ctx.IDENTIFIER():
            name_token = ctx.IDENTIFIER().getSymbol()
            if name_token.text not in self.skip_names:
                new_name = self._rename(name_token.text, ctx, is_func=True)
                self.rewriter.replaceSingleToken(name_token, new_name)
        self.visitChildren(ctx)
        return None

    def visitParam(self, ctx):
        if hasattr(ctx, "IDENTIFIER") and ctx.IDENTIFIER():
            name_token = ctx.IDENTIFIER().getSymbol()
            if name_token.text not in self.skip_names:
                new_name = self._rename(name_token.text, ctx, is_func=False)
                self.rewriter.replaceSingleToken(name_token, new_name)
        return None

    def visitInitDeclarator(self, ctx):
        if hasattr(ctx, "IDENTIFIER") and ctx.IDENTIFIER():
            name_token = ctx.IDENTIFIER().getSymbol()
            if name_token.text not in self.skip_names:
                new_name = self._rename(name_token.text, ctx, is_func=False)
                self.rewriter.replaceSingleToken(name_token, new_name)
        self.visitChildren(ctx)
        return None

    # Note: we intentionally do NOT rely solely on PrimaryExpr visits to rename usages because
    # function calls and other contexts may have different parse shapes. We will perform a
    # token-level replacement after visiting to be sure all occurrences are handled.

def renamer(input_path, output_path):
    """
    Reads input_path, performs semantic renaming (functions/variables that are declared),
    then performs a token-level replacement of all IDENTIFIER tokens that appear in the
    mapping. Writes result to output_path.
    """
    input_stream = FileStream(input_path, encoding="utf-8")
    lexer = MiniCLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiniCParser(tokens)
    tree = parser.program()

    visitor = SemanticRenameVisitor(tokens)
    visitor.visit(tree)

    # Global token-level replacement: replace every IDENTIFIER token that is in name_map.
    # This ensures function calls and any other identifier usage are renamed consistently.
    for t in tokens.tokens:
        # skip None, EOF, or tokens without 'text' attr
        if not hasattr(t, "type") or not hasattr(t, "text"):
            continue
        if t.type == MiniCLexer.IDENTIFIER:
            original = t.text
            # don't replace skipped names even if they accidentally exist in map
            if original in visitor.name_map and original not in visitor.skip_names:
                visitor.rewriter.replaceSingleToken(t, visitor.name_map[original])

    # write final text
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(visitor.rewriter.getDefaultText())
