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
        self.selector_name = "selector_" + str(random.randint(1000, 9999))
        self.counter = 1

    def visitFunctionDecl(self, ctx):
        if ctx.IDENTIFIER().getText() == "main":
            self._flatten_main_function(ctx)
        return self.visitChildren(ctx)

    def _flatten_main_function(self, ctx):
        block = ctx.compoundStmt()
        stmts = block.statement()

        selector_value = self.counter
        init_code = f"int {self.selector_name} = {selector_value};\n"

        switch_code = f"while ({self.selector_name} > 0) {{\n\tswitch({self.selector_name}) {{\n"

        for stmt in stmts:
            case_num = self.counter

            start_index = stmt.start.tokenIndex
            stop_index = stmt.stop.tokenIndex
            case_code = self.token_stream.getText(start_index, stop_index)

            switch_case = (
                f"\t\tcase {case_num}:\n"
                f"\t\t\t{case_code}\n"
                f"\t\t\t{self.selector_name} = {case_num + 1};\n"
                f"\t\t\tbreak;\n"
            )

            switch_code += switch_case
            self.counter += 1

        switch_code += (
            f"\t\tcase {self.counter}:\n"
            f"\t\t\t{self.selector_name} = 0;\n"
            f"\t\t\tbreak;\n"
            f"\t}}\n}}\n"
        )

        full_new_code = "{" + "\n\t" + init_code + "\n\t" + switch_code + "}"
        self.rewriter.replaceRange(block.start.tokenIndex, block.stop.tokenIndex, full_new_code)

    def visitChildren(self, node):
        result = None
        for child in node.getChildren():
            result = child.accept(self)
        return result


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
