from antlr4 import FileStream, CommonTokenStream
from src.Grammar.MiniCLexer import MiniCLexer
from src.Grammar.MiniCParser import MiniCParser
from src.ASTBuilder import ASTBuilder

input_file = "input.mc"
lexer = MiniCLexer(FileStream(input_file))
stream = CommonTokenStream(lexer)
parser = MiniCParser(stream)

tree = parser.program()
builder = ASTBuilder()
ast = builder.visit(tree)

print(ast)  # or use a pretty printer
