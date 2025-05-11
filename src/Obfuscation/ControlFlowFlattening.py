import random
from antlr4 import *
from src.Grammar.MiniCLexer import MiniCLexer
from src.Grammar.MiniCParser import MiniCParser
from src.Grammar.MiniCVisitor import MiniCVisitor
from antlr4.TokenStreamRewriter import TokenStreamRewriter

class ControlFlowFlattener(MiniCVisitor):
    def __init__(self, token_stream):
        self.rewriter = TokenStreamRewriter(token_stream)
        self.token_stream = token_stream

    def visitFunctionDef(self, ctx):
        if ctx.IDENTIFIER().getText() != "main":
            return self.visitChildren(ctx)

        compound = ctx.compoundStmt()
        stmts = compound.blockItemList().blockItem()

        selector_var = "_cf_selector"
        new_code = f"\n\tint {selector_var} = 1;\n\twhile ({selector_var} > 0) {{\n\t\tswitch({selector_var}) {{\n"

        for i, stmt in enumerate(stmts):
            case_index = i + 1
            original_code = self.token_stream.getText(stmt.start, stmt.stop)
            new_code += f"\t\t\tcase {case_index}:\n\t\t\t\t{original_code}\n\t\t\t\t{selector_var} = {case_index + 1};\n\t\t\t\tbreak;\n"

        new_code += f"\t\t\tcase {len(stmts) + 1}:\n\t\t\t\t{selector_var} = 0;\n\t\t\t\tbreak;\n"
        new_code += "\t\t}\n\t}\n"

        start_idx = compound.start.tokenIndex
        stop_idx = compound.stop.tokenIndex
        self.rewriter.replaceRange(start_idx, stop_idx, "{\n" + new_code + "}")

        return None


def control_flow_flattening(input_path, output_path):
    input_stream = FileStream(input_path, encoding="utf-8")
    lexer = MiniCLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiniCParser(tokens)
    tree = parser.program()

    flattener = ControlFlowFlattener(tokens)
    flattener.visit(tree)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(flattener.rewriter.getDefaultText())