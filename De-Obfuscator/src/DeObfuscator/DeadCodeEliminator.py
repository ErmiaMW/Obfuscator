from collections import defaultdict
from antlr4 import *
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from src.Grammar.MiniCLexer import MiniCLexer
from src.Grammar.MiniCParser import MiniCParser
from src.Grammar.MiniCVisitor import MiniCVisitor


class DeadCodeCleaner(MiniCVisitor):
    def __init__(self, token_stream):
        self.rewriter = TokenStreamRewriter(token_stream)
        self.token_stream = token_stream
        self.tokens = token_stream.tokens

        self.scope_stack = ["$global"]
        self.func_declared_vars = defaultdict(list)
        self.func_used_vars = defaultdict(set)

        self.declared_funcs = {}
        self.called_funcs = set()

    def visitSelectionStmt(self, ctx: MiniCParser.SelectionStmtContext):
        cond = ctx.expression().getText().strip()
        if cond in {"0", "false"}:
            self.rewriter.delete("default", ctx.start.tokenIndex, ctx.stop.tokenIndex)
            return None
        return self.visitChildren(ctx)

    def visitIterationStmt(self, ctx: MiniCParser.IterationStmtContext):
        text = ctx.getText().replace(" ", "")
        if text.startswith("while(0)"):
            self.rewriter.delete("default", ctx.start.tokenIndex, ctx.stop.tokenIndex)
            return None
        return self.visitChildren(ctx)

    def visitFunctionDecl(self, ctx: MiniCParser.FunctionDeclContext):
        func_name = ctx.IDENTIFIER().getText()
        self.declared_funcs[func_name] = (ctx, ctx.start.tokenIndex, ctx.stop.tokenIndex)

        self.scope_stack.append(func_name)
        try:
            _ = self.func_declared_vars[func_name]
            _ = self.func_used_vars[func_name]
            return self.visitChildren(ctx)
        finally:
            self.scope_stack.pop()

    def visitDeclaration(self, ctx: MiniCParser.DeclarationContext):
        scope = self.scope_stack[-1]
        init_list = list(ctx.initDeclaratorList().initDeclarator())
        for idx, initDecl in enumerate(init_list):
            var_name = initDecl.IDENTIFIER().getText()
            self.func_declared_vars[scope].append({
                "var": var_name,
                "decl_ctx": ctx,
                "init_ctx": initDecl,
                "decl_start": ctx.start.tokenIndex,
                "decl_stop": ctx.stop.tokenIndex,
                "init_start": initDecl.start.tokenIndex,
                "init_stop": initDecl.stop.tokenIndex,
                "order": idx
            })
        return self.visitChildren(ctx)

    def visitPrimaryExpr(self, ctx: MiniCParser.PrimaryExprContext):
        if ctx.IDENTIFIER():
            ident = ctx.IDENTIFIER().getText()
            is_call = (ctx.getChildCount() >= 2 and ctx.getChild(1).getText() == '(')
            if is_call:
                self.called_funcs.add(ident)
            else:
                scope = self.scope_stack[-1]
                self.func_used_vars[scope].add(ident)
        return self.visitChildren(ctx)

    def clean_unused_variables(self):
        for scope, records in self.func_declared_vars.items():
            by_decl = defaultdict(list)
            for r in records:
                by_decl[id(r["decl_ctx"])].append(r)

            for group in by_decl.values():
                group.sort(key=lambda r: r["order"])
                used = self.func_used_vars[scope]
                all_names = [r["var"] for r in group]
                unused_flags = [name not in used for name in all_names]

                if all(unused_flags):
                    start = group[0]["decl_start"]
                    stop = group[0]["decl_stop"]
                    self.rewriter.delete("default", start, stop)
                    continue

                n = len(group)
                for i, r in enumerate(group):
                    if not unused_flags[i]:
                        continue
                    if i < n - 1:
                        del_start = r["init_start"]
                        next_start = group[i + 1]["init_start"]
                        del_stop = next_start - 1
                    else:
                        prev_stop = group[i - 1]["init_stop"] if i > 0 else r["init_start"] - 1
                        comma_idx = None
                        a = prev_stop + 1
                        b = r["init_start"] - 1
                        if a <= b:
                            for t in self.tokens[a:b + 1]:
                                if t.text == ',':
                                    comma_idx = t.tokenIndex
                                    break
                        del_start = comma_idx if comma_idx is not None else r["init_start"]
                        del_stop = r["init_stop"]
                    self.rewriter.delete("default", del_start, del_stop)

    def clean_unused_functions(self):
        for func_name, (ctx, start_idx, stop_idx) in sorted(
            self.declared_funcs.items(),
            key=lambda x: x[1][0].start.tokenIndex,
            reverse=True,
        ):
            if func_name != 'main' and func_name not in self.called_funcs:
                self.rewriter.delete("default", start_idx, stop_idx)


def delete_dead_code(input_path, output_path):
    input_stream = FileStream(input_path, encoding="utf-8")
    lexer = MiniCLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiniCParser(tokens)
    tree = parser.program()

    cleaner = DeadCodeCleaner(tokens)
    cleaner.visit(tree)
    cleaner.clean_unused_variables()
    cleaner.clean_unused_functions()

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(cleaner.rewriter.getDefaultText())