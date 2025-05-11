import random
from antlr4 import *
from src.Grammar.MiniCLexer import MiniCLexer
from src.Grammar.MiniCParser import MiniCParser
from src.Grammar.MiniCVisitor import MiniCVisitor
from antlr4.TokenStreamRewriter import TokenStreamRewriter

class DeadCodeInjector(MiniCVisitor):
    def __init__(self, token_stream):
        self.rewriter = TokenStreamRewriter(token_stream)
        self.token_stream = token_stream
        self.known_vars = set()

    def _random_var_name(self):
        return  ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(3, 10)))

    def _random_value(self, typ):
        if typ == 'int':
            return str(random.randint(-100, 100))
        elif typ == 'char':
            return "'" + random.choice('abcdefghijklmnopqrstuvwxyz') + "'"
        elif typ == 'bool':
            return random.choice(['true', 'false'])

    def _generate_dead_code(self):
        wrapper = random.choice(['if (0)', 'while (0)', 'if (false)'])

        # Generate 1–3 dead inner statements (with known vars if possible)
        dead_lines = []
        for _ in range(random.randint(1, 3)):
            if self.known_vars:
                var = random.choice(list(self.known_vars))
                expr = f'{var} = {random.randint(1, 100)};'
                dead_lines.append(f'\t\t{expr}')  # 2 tabs inside block
            else:
                typ = random.choice(['int', 'char', 'bool'])
                name = self._random_var_name()
                value = self._random_value(typ)
                dead_lines.append(f'\t\t{typ} {name} = {value};')  # 2 tabs inside block

        # Build the block
        block = f"\t{wrapper} {{\n" + '\n'.join(dead_lines) + "\n\t}"

        # Add 1–2 unused variable declarations outside the block (1 tab)
        for _ in range(random.randint(1, 2)):
            typ = random.choice(['int', 'char', 'bool'])
            name = self._random_var_name()
            value = self._random_value(typ)
            block += f"\n\t{typ} {name} = {value};"

        return block



    def visitInitDeclarator(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        self.known_vars.add(var_name)
        return self.visitChildren(ctx)

    def visitStatement(self, ctx):
        stop_token = ctx.stop
        dead_code = self._generate_dead_code()
        self.rewriter.insertAfter(stop_token.tokenIndex, "\n" + dead_code + "\n")
        return self.visitChildren(ctx)



def inject_dead_code(input_path, output_path):
    input_stream = FileStream(input_path, encoding="utf-8")
    lexer = MiniCLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiniCParser(tokens)
    tree = parser.program()

    injector = DeadCodeInjector(tokens)
    injector.visit(tree)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(injector.rewriter.getDefaultText())
