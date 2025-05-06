# main.py
from antlr4 import *
from src.Grammar.MiniCLexer import MiniCLexer
from src.Grammar.MiniCParser import MiniCParser

def main():
    input_stream = FileStream("input.mc")
    lexer = MiniCLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniCParser(token_stream)
    tree = parser.program()  # start rule
    print(tree.toStringTree(recog=parser))

if __name__ == "__main__":
    main()
