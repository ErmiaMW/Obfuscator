import random
from antlr4 import *
from src.Grammar.MiniCLexer import MiniCLexer
from src.Grammar.MiniCParser import MiniCParser
from src.Grammar.MiniCVisitor import MiniCVisitor
from antlr4.TokenStreamRewriter import TokenStreamRewriter

class DummyFunctionInjector(MiniCVisitor):
    def __init__(self, token_stream):
        self.rewriter = TokenStreamRewriter(token_stream)
        self.token_stream = token_stream
        self.injected = False

    def _generate_dummy_function(self) -> str:
        name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=6))
        
        dummy_code = f"""
int {name}() {{
    int x = {random.randint(1, 100)};
    int y = {random.randint(1, 100)};    
    if (x % 2 == 0) {{
        int y = 1;
        for (int i = 0; i < 3; i++) {{
            y *= i + 1;
        }}
        x += y;
    }} else {{
        int temp = 0;
        while (temp < 5) {{
            x += temp;
            temp++;
        }}
    }}
    int z = x + y;
    return z*4;
}}"""

        return dummy_code.strip()

    def visitFunctionDecl(self, ctx):
        stop_index = ctx.stop.tokenIndex
        dummy_code = "\n\n" + self._generate_dummy_function() + "\n"
        self.rewriter.insertAfter(stop_index, dummy_code)
        self.injected = True
        return self.visitChildren(ctx)

def dummy_function(input_path, output_path):
    input_stream = FileStream(input_path, encoding="utf-8")
    lexer = MiniCLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiniCParser(tokens)
    tree = parser.program()

    injector = DummyFunctionInjector(tokens)
    injector.visit(tree)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(injector.rewriter.getDefaultText())
