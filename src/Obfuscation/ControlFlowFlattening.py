from antlr4 import *
from src.Grammar.MiniCLexer import MiniCLexer
from src.Grammar.MiniCParser import MiniCParser
from src.Grammar.MiniCVisitor import MiniCVisitor
from antlr4.TokenStreamRewriter import TokenStreamRewriter

class ControlFlowFlattener(MiniCVisitor):
    def __init__(self, token_stream):
        self.rewriter = TokenStreamRewriter(token_stream)
        self.token_stream = token_stream

    def visitFunctionDecl(self, ctx):
        # فقط تابع main را تغییر بده
        func_name = ctx.IDENTIFIER().getText()
        if func_name != "main":
            return self.visitChildren(ctx)

        compound = ctx.compoundStmt()

        # استخراج تمام بلاک‌های statement داخل تابع main
        statements = []
        for child in compound.children:
            if isinstance(child, MiniCParser.StatementContext):
                statements.append(child)

        # اگر بدنه‌ای نداشت، کاری نکن
        if not statements:
            return self.visitChildren(ctx)

        selector_var = "__cf_selector"
        flattened_code = f"\n\tint {selector_var} = 1;\n\twhile ({selector_var} > 0) {{\n\t\tswitch({selector_var}) {{\n"

        for idx, stmt in enumerate(statements):
            stmt_text = self.token_stream.getText(stmt.start, stmt.stop)
            next_selector = idx + 2 if idx < len(statements) - 1 else 0  # آخرین case به 0 ختم می‌شود
            flattened_code += (
                f"\t\t\tcase {idx+1}:\n"
                f"\t\t\t\t{stmt_text}\n"
                f"\t\t\t\t{selector_var} = {next_selector};\n"
                f"\t\t\t\tbreak;\n"
            )

        flattened_code += "\t\t}\n\t}\n"

        # جایگزین کردن کل بدنه تابع main با ساختار flatten‌شده
        self.rewriter.replaceRange(compound.start.tokenIndex, compound.stop.tokenIndex, "{\n" + flattened_code + "}")

        return None


def control_flow_flattening(input_path, output_path):
    input_stream = FileStream(input_path, encoding="utf-8")
    lexer = MiniCLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiniCParser(tokens)
    tree = parser.program()

    visitor = ControlFlowFlattener(tokens)
    visitor.visit(tree)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(visitor.rewriter.getDefaultText())
