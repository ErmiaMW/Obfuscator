from antlr4 import *
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from src.Grammar.MiniCLexer import MiniCLexer
from src.Grammar.MiniCParser import MiniCParser
from src.Grammar.MiniCVisitor import MiniCVisitor

class DeadCodeAnalyzer(MiniCVisitor):
    def __init__(self, token_stream):
        self.scope_vars = [{}]
        self.to_delete = []
        self.tokens = token_stream

    def visitCompoundStmt(self, ctx: MiniCParser.CompoundStmtContext):
        self.scope_vars.append({})
        self.visitChildren(ctx)
        current_scope = self.scope_vars.pop()
        
        for var_name, decl_info in current_scope.items():
            if not decl_info['used']:
                self.to_delete.append((decl_info['start_token_index'], decl_info['stop_token_index']))
    
    def visitDeclaration(self, ctx: MiniCParser.DeclarationContext):
        init_declarators = ctx.initDeclaratorList().initDeclarator()
        
        for declarator in init_declarators:
            var_name = declarator.IDENTIFIER().getText()
            self.scope_vars[-1][var_name] = {
                'used': False,
                'start_token_index': ctx.start.tokenIndex,
                'stop_token_index': ctx.stop.tokenIndex
            }
        return self.visitChildren(ctx)

    def visitPrimaryExpr(self, ctx: MiniCParser.PrimaryExprContext):
        identifier = ctx.IDENTIFIER()
        if identifier:
            var_name = identifier.getText()
            for scope in reversed(self.scope_vars):
                if var_name in scope:
                    scope[var_name]['used'] = True
                    break
        return self.visitChildren(ctx)

    def visitSelectionStmt(self, ctx: MiniCParser.SelectionStmtContext):
        expr_ctx = ctx.expression()
        if expr_ctx and expr_ctx.getText() in ['0', 'false']:
            self.to_delete.append((ctx.start.tokenIndex, ctx.stop.tokenIndex))
            return None
        return self.visitChildren(ctx)

    def visitIterationStmt(self, ctx: MiniCParser.IterationStmtContext):
        if ctx.while_clause() and ctx.expression(0).getText() == '0':
            self.to_delete.append((ctx.start.tokenIndex, ctx.stop.tokenIndex))
            return None
        return self.visitChildren(ctx)
        
    def visitReturnStmt(self, ctx: MiniCParser.ReturnStmtContext):
        return self.visitChildren(ctx)

def delete_dead_code(input_path, output_path):
    input_stream = FileStream(input_path, encoding="utf-8")
    lexer = MiniCLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiniCParser(tokens)
    tree = parser.program()

    analyzer = DeadCodeAnalyzer(tokens)
    analyzer.visit(tree)

    rewriter = TokenStreamRewriter(tokens)
    
    # Sort the list of deletions in reverse order by their starting index
    sorted_deletions = sorted(analyzer.to_delete, key=lambda x: x[0], reverse=True)
    
    for start, stop in sorted_deletions:
        # Unpack the tuple and pass both arguments to the delete method
        rewriter.delete(start, stop)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rewriter.getDefaultText())