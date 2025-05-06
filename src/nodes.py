class ProgramNode:
    def __init__(self, declarations):
        self.declarations = declarations  # list of FunctionDeclNode or VarDeclNode

class FunctionDeclNode:
    def __init__(self, return_type, name, params, body):
        self.return_type = return_type
        self.name = name
        self.params = params  # list of ParamNode
        self.body = body      # list of StatementNode

class ParamNode:
    def __init__(self, type_, name):
        self.type = type_
        self.name = name

class VarDeclNode:
    def __init__(self, type_, name, init_expr=None):
        self.type = type_
        self.name = name
        self.init_expr = init_expr

class CompoundStmtNode:
    def __init__(self, statements):
        self.statements = statements  # list of StatementNode

class ExpressionStmtNode:
    def __init__(self, expr):
        self.expr = expr

class IfNode:
    def __init__(self, condition, then_stmt, else_stmt=None):
        self.condition = condition
        self.then_stmt = then_stmt
        self.else_stmt = else_stmt

class WhileNode:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class ForNode:
    def __init__(self, init, cond, post, body):
        self.init = init
        self.cond = cond
        self.post = post
        self.body = body

class ReturnNode:
    def __init__(self, expr):
        self.expr = expr

class IONode:
    def __init__(self, kind, format_str, args):
        self.kind = kind  # 'printf' or 'scanf'
        self.format_str = format_str
        self.args = args  # list of ExprNode

class AssignmentNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class BinaryOpNode:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class UnaryOpNode:
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand

class LiteralNode:
    def __init__(self, value):
        self.value = value

class IdentifierNode:
    def __init__(self, name):
        self.name = name

class FunctionCallNode:
    def __init__(self, name, args):
        self.name = name
        self.args = args
