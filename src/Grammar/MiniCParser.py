# Generated from Grammar/MiniC.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,40,276,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,1,0,5,
        0,55,8,0,10,0,12,0,58,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,66,8,1,1,1,
        1,1,1,1,1,2,1,2,1,2,5,2,74,8,2,10,2,12,2,77,9,2,1,3,1,3,1,3,1,4,
        1,4,1,4,1,4,1,5,1,5,1,5,5,5,89,8,5,10,5,12,5,92,9,5,1,6,1,6,1,6,
        3,6,97,8,6,1,7,1,7,1,8,1,8,1,8,5,8,104,8,8,10,8,12,8,107,9,8,1,8,
        1,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,117,8,9,1,10,3,10,120,8,10,1,10,
        1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,131,8,11,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,142,8,12,1,12,1,12,3,12,
        146,8,12,1,12,1,12,3,12,150,8,12,1,12,1,12,3,12,154,8,12,1,13,1,
        13,3,13,158,8,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,5,14,167,8,14,
        10,14,12,14,170,9,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,179,
        8,14,1,14,5,14,182,8,14,10,14,12,14,185,9,14,1,14,1,14,3,14,189,
        8,14,1,15,1,15,1,16,1,16,1,16,3,16,196,8,16,1,17,1,17,1,17,5,17,
        201,8,17,10,17,12,17,204,9,17,1,18,1,18,1,18,5,18,209,8,18,10,18,
        12,18,212,9,18,1,19,1,19,1,19,5,19,217,8,19,10,19,12,19,220,9,19,
        1,20,1,20,1,20,5,20,225,8,20,10,20,12,20,228,9,20,1,21,1,21,1,21,
        5,21,233,8,21,10,21,12,21,236,9,21,1,22,1,22,1,22,5,22,241,8,22,
        10,22,12,22,244,9,22,1,23,1,23,1,23,3,23,249,8,23,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,1,24,3,24,259,8,24,1,24,1,24,1,24,1,24,1,24,
        3,24,266,8,24,1,25,1,25,1,25,5,25,271,8,25,10,25,12,25,274,9,25,
        1,25,0,0,26,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,50,0,6,1,0,6,8,1,0,21,22,1,0,23,26,1,0,27,28,1,
        0,29,31,2,0,27,28,32,32,289,0,56,1,0,0,0,2,61,1,0,0,0,4,70,1,0,0,
        0,6,78,1,0,0,0,8,81,1,0,0,0,10,85,1,0,0,0,12,93,1,0,0,0,14,98,1,
        0,0,0,16,100,1,0,0,0,18,116,1,0,0,0,20,119,1,0,0,0,22,123,1,0,0,
        0,24,153,1,0,0,0,26,155,1,0,0,0,28,188,1,0,0,0,30,190,1,0,0,0,32,
        192,1,0,0,0,34,197,1,0,0,0,36,205,1,0,0,0,38,213,1,0,0,0,40,221,
        1,0,0,0,42,229,1,0,0,0,44,237,1,0,0,0,46,248,1,0,0,0,48,265,1,0,
        0,0,50,267,1,0,0,0,52,55,3,2,1,0,53,55,3,8,4,0,54,52,1,0,0,0,54,
        53,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,59,1,0,0,
        0,58,56,1,0,0,0,59,60,5,0,0,1,60,1,1,0,0,0,61,62,3,14,7,0,62,63,
        5,37,0,0,63,65,5,1,0,0,64,66,3,4,2,0,65,64,1,0,0,0,65,66,1,0,0,0,
        66,67,1,0,0,0,67,68,5,2,0,0,68,69,3,16,8,0,69,3,1,0,0,0,70,75,3,
        6,3,0,71,72,5,3,0,0,72,74,3,6,3,0,73,71,1,0,0,0,74,77,1,0,0,0,75,
        73,1,0,0,0,75,76,1,0,0,0,76,5,1,0,0,0,77,75,1,0,0,0,78,79,3,14,7,
        0,79,80,5,37,0,0,80,7,1,0,0,0,81,82,3,14,7,0,82,83,3,10,5,0,83,84,
        5,4,0,0,84,9,1,0,0,0,85,90,3,12,6,0,86,87,5,3,0,0,87,89,3,12,6,0,
        88,86,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,11,1,
        0,0,0,92,90,1,0,0,0,93,96,5,37,0,0,94,95,5,5,0,0,95,97,3,30,15,0,
        96,94,1,0,0,0,96,97,1,0,0,0,97,13,1,0,0,0,98,99,7,0,0,0,99,15,1,
        0,0,0,100,105,5,9,0,0,101,104,3,8,4,0,102,104,3,18,9,0,103,101,1,
        0,0,0,103,102,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,
        0,0,0,106,108,1,0,0,0,107,105,1,0,0,0,108,109,5,10,0,0,109,17,1,
        0,0,0,110,117,3,20,10,0,111,117,3,16,8,0,112,117,3,22,11,0,113,117,
        3,24,12,0,114,117,3,26,13,0,115,117,3,28,14,0,116,110,1,0,0,0,116,
        111,1,0,0,0,116,112,1,0,0,0,116,113,1,0,0,0,116,114,1,0,0,0,116,
        115,1,0,0,0,117,19,1,0,0,0,118,120,3,30,15,0,119,118,1,0,0,0,119,
        120,1,0,0,0,120,121,1,0,0,0,121,122,5,4,0,0,122,21,1,0,0,0,123,124,
        5,11,0,0,124,125,5,1,0,0,125,126,3,30,15,0,126,127,5,2,0,0,127,130,
        3,18,9,0,128,129,5,12,0,0,129,131,3,18,9,0,130,128,1,0,0,0,130,131,
        1,0,0,0,131,23,1,0,0,0,132,133,5,13,0,0,133,134,5,1,0,0,134,135,
        3,30,15,0,135,136,5,2,0,0,136,137,3,18,9,0,137,154,1,0,0,0,138,139,
        5,14,0,0,139,141,5,1,0,0,140,142,3,30,15,0,141,140,1,0,0,0,141,142,
        1,0,0,0,142,143,1,0,0,0,143,145,5,4,0,0,144,146,3,30,15,0,145,144,
        1,0,0,0,145,146,1,0,0,0,146,147,1,0,0,0,147,149,5,4,0,0,148,150,
        3,30,15,0,149,148,1,0,0,0,149,150,1,0,0,0,150,151,1,0,0,0,151,152,
        5,2,0,0,152,154,3,18,9,0,153,132,1,0,0,0,153,138,1,0,0,0,154,25,
        1,0,0,0,155,157,5,15,0,0,156,158,3,30,15,0,157,156,1,0,0,0,157,158,
        1,0,0,0,158,159,1,0,0,0,159,160,5,4,0,0,160,27,1,0,0,0,161,162,5,
        16,0,0,162,163,5,1,0,0,163,168,5,35,0,0,164,165,5,3,0,0,165,167,
        3,30,15,0,166,164,1,0,0,0,167,170,1,0,0,0,168,166,1,0,0,0,168,169,
        1,0,0,0,169,171,1,0,0,0,170,168,1,0,0,0,171,172,5,2,0,0,172,189,
        5,4,0,0,173,174,5,17,0,0,174,175,5,1,0,0,175,183,5,35,0,0,176,178,
        5,3,0,0,177,179,5,18,0,0,178,177,1,0,0,0,178,179,1,0,0,0,179,180,
        1,0,0,0,180,182,5,37,0,0,181,176,1,0,0,0,182,185,1,0,0,0,183,181,
        1,0,0,0,183,184,1,0,0,0,184,186,1,0,0,0,185,183,1,0,0,0,186,187,
        5,2,0,0,187,189,5,4,0,0,188,161,1,0,0,0,188,173,1,0,0,0,189,29,1,
        0,0,0,190,191,3,32,16,0,191,31,1,0,0,0,192,195,3,34,17,0,193,194,
        5,5,0,0,194,196,3,32,16,0,195,193,1,0,0,0,195,196,1,0,0,0,196,33,
        1,0,0,0,197,202,3,36,18,0,198,199,5,19,0,0,199,201,3,36,18,0,200,
        198,1,0,0,0,201,204,1,0,0,0,202,200,1,0,0,0,202,203,1,0,0,0,203,
        35,1,0,0,0,204,202,1,0,0,0,205,210,3,38,19,0,206,207,5,20,0,0,207,
        209,3,38,19,0,208,206,1,0,0,0,209,212,1,0,0,0,210,208,1,0,0,0,210,
        211,1,0,0,0,211,37,1,0,0,0,212,210,1,0,0,0,213,218,3,40,20,0,214,
        215,7,1,0,0,215,217,3,40,20,0,216,214,1,0,0,0,217,220,1,0,0,0,218,
        216,1,0,0,0,218,219,1,0,0,0,219,39,1,0,0,0,220,218,1,0,0,0,221,226,
        3,42,21,0,222,223,7,2,0,0,223,225,3,42,21,0,224,222,1,0,0,0,225,
        228,1,0,0,0,226,224,1,0,0,0,226,227,1,0,0,0,227,41,1,0,0,0,228,226,
        1,0,0,0,229,234,3,44,22,0,230,231,7,3,0,0,231,233,3,44,22,0,232,
        230,1,0,0,0,233,236,1,0,0,0,234,232,1,0,0,0,234,235,1,0,0,0,235,
        43,1,0,0,0,236,234,1,0,0,0,237,242,3,46,23,0,238,239,7,4,0,0,239,
        241,3,46,23,0,240,238,1,0,0,0,241,244,1,0,0,0,242,240,1,0,0,0,242,
        243,1,0,0,0,243,45,1,0,0,0,244,242,1,0,0,0,245,246,7,5,0,0,246,249,
        3,46,23,0,247,249,3,48,24,0,248,245,1,0,0,0,248,247,1,0,0,0,249,
        47,1,0,0,0,250,266,5,37,0,0,251,266,5,36,0,0,252,266,5,34,0,0,253,
        266,5,33,0,0,254,266,5,35,0,0,255,256,5,37,0,0,256,258,5,1,0,0,257,
        259,3,50,25,0,258,257,1,0,0,0,258,259,1,0,0,0,259,260,1,0,0,0,260,
        266,5,2,0,0,261,262,5,1,0,0,262,263,3,30,15,0,263,264,5,2,0,0,264,
        266,1,0,0,0,265,250,1,0,0,0,265,251,1,0,0,0,265,252,1,0,0,0,265,
        253,1,0,0,0,265,254,1,0,0,0,265,255,1,0,0,0,265,261,1,0,0,0,266,
        49,1,0,0,0,267,272,3,30,15,0,268,269,5,3,0,0,269,271,3,30,15,0,270,
        268,1,0,0,0,271,274,1,0,0,0,272,270,1,0,0,0,272,273,1,0,0,0,273,
        51,1,0,0,0,274,272,1,0,0,0,31,54,56,65,75,90,96,103,105,116,119,
        130,141,145,149,153,157,168,178,183,188,195,202,210,218,226,234,
        242,248,258,265,272
    ]

class MiniCParser ( Parser ):

    grammarFileName = "MiniC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "';'", "'='", "'int'", 
                     "'char'", "'bool'", "'{'", "'}'", "'if'", "'else'", 
                     "'while'", "'for'", "'return'", "'printf'", "'scanf'", 
                     "'&'", "'||'", "'&&'", "'=='", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BOOL", "CHAR", "STRING", "NUMBER", "IDENTIFIER", 
                      "WS", "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_functionDecl = 1
    RULE_params = 2
    RULE_param = 3
    RULE_declaration = 4
    RULE_initDeclaratorList = 5
    RULE_initDeclarator = 6
    RULE_typeSpecifier = 7
    RULE_compoundStmt = 8
    RULE_statement = 9
    RULE_expressionStmt = 10
    RULE_selectionStmt = 11
    RULE_iterationStmt = 12
    RULE_returnStmt = 13
    RULE_ioStmt = 14
    RULE_expression = 15
    RULE_assignmentExpr = 16
    RULE_logicalOrExpr = 17
    RULE_logicalAndExpr = 18
    RULE_equalityExpr = 19
    RULE_relationalExpr = 20
    RULE_additiveExpr = 21
    RULE_multiplicativeExpr = 22
    RULE_unaryExpr = 23
    RULE_primaryExpr = 24
    RULE_argumentList = 25

    ruleNames =  [ "program", "functionDecl", "params", "param", "declaration", 
                   "initDeclaratorList", "initDeclarator", "typeSpecifier", 
                   "compoundStmt", "statement", "expressionStmt", "selectionStmt", 
                   "iterationStmt", "returnStmt", "ioStmt", "expression", 
                   "assignmentExpr", "logicalOrExpr", "logicalAndExpr", 
                   "equalityExpr", "relationalExpr", "additiveExpr", "multiplicativeExpr", 
                   "unaryExpr", "primaryExpr", "argumentList" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    BOOL=33
    CHAR=34
    STRING=35
    NUMBER=36
    IDENTIFIER=37
    WS=38
    LINE_COMMENT=39
    BLOCK_COMMENT=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniCParser.EOF, 0)

        def functionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.FunctionDeclContext)
            else:
                return self.getTypedRuleContext(MiniCParser.FunctionDeclContext,i)


        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(MiniCParser.DeclarationContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0):
                self.state = 54
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 52
                    self.functionDecl()
                    pass

                elif la_ == 2:
                    self.state = 53
                    self.declaration()
                    pass


                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
            self.match(MiniCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(MiniCParser.TypeSpecifierContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniCParser.IDENTIFIER, 0)

        def compoundStmt(self):
            return self.getTypedRuleContext(MiniCParser.CompoundStmtContext,0)


        def params(self):
            return self.getTypedRuleContext(MiniCParser.ParamsContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = MiniCParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.typeSpecifier()
            self.state = 62
            self.match(MiniCParser.IDENTIFIER)
            self.state = 63
            self.match(MiniCParser.T__0)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0):
                self.state = 64
                self.params()


            self.state = 67
            self.match(MiniCParser.T__1)
            self.state = 68
            self.compoundStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.ParamContext)
            else:
                return self.getTypedRuleContext(MiniCParser.ParamContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = MiniCParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.param()
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 71
                self.match(MiniCParser.T__2)
                self.state = 72
                self.param()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(MiniCParser.TypeSpecifierContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniCParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniCParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MiniCParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.typeSpecifier()
            self.state = 79
            self.match(MiniCParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(MiniCParser.TypeSpecifierContext,0)


        def initDeclaratorList(self):
            return self.getTypedRuleContext(MiniCParser.InitDeclaratorListContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MiniCParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.typeSpecifier()
            self.state = 82
            self.initDeclaratorList()
            self.state = 83
            self.match(MiniCParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitDeclaratorListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initDeclarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.InitDeclaratorContext)
            else:
                return self.getTypedRuleContext(MiniCParser.InitDeclaratorContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_initDeclaratorList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitDeclaratorList" ):
                listener.enterInitDeclaratorList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitDeclaratorList" ):
                listener.exitInitDeclaratorList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitDeclaratorList" ):
                return visitor.visitInitDeclaratorList(self)
            else:
                return visitor.visitChildren(self)




    def initDeclaratorList(self):

        localctx = MiniCParser.InitDeclaratorListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_initDeclaratorList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.initDeclarator()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 86
                self.match(MiniCParser.T__2)
                self.state = 87
                self.initDeclarator()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitDeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniCParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_initDeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitDeclarator" ):
                listener.enterInitDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitDeclarator" ):
                listener.exitInitDeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitDeclarator" ):
                return visitor.visitInitDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def initDeclarator(self):

        localctx = MiniCParser.InitDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_initDeclarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(MiniCParser.IDENTIFIER)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 94
                self.match(MiniCParser.T__4)
                self.state = 95
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniCParser.RULE_typeSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSpecifier" ):
                listener.enterTypeSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSpecifier" ):
                listener.exitTypeSpecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSpecifier" ):
                return visitor.visitTypeSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def typeSpecifier(self):

        localctx = MiniCParser.TypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typeSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(MiniCParser.DeclarationContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniCParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_compoundStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundStmt" ):
                listener.enterCompoundStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundStmt" ):
                listener.exitCompoundStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompoundStmt" ):
                return visitor.visitCompoundStmt(self)
            else:
                return visitor.visitChildren(self)




    def compoundStmt(self):

        localctx = MiniCParser.CompoundStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_compoundStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(MiniCParser.T__8)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 270985849810) != 0):
                self.state = 103
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6, 7, 8]:
                    self.state = 101
                    self.declaration()
                    pass
                elif token in [1, 4, 9, 11, 13, 14, 15, 16, 17, 27, 28, 32, 33, 34, 35, 36, 37]:
                    self.state = 102
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
            self.match(MiniCParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionStmt(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionStmtContext,0)


        def compoundStmt(self):
            return self.getTypedRuleContext(MiniCParser.CompoundStmtContext,0)


        def selectionStmt(self):
            return self.getTypedRuleContext(MiniCParser.SelectionStmtContext,0)


        def iterationStmt(self):
            return self.getTypedRuleContext(MiniCParser.IterationStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(MiniCParser.ReturnStmtContext,0)


        def ioStmt(self):
            return self.getTypedRuleContext(MiniCParser.IoStmtContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 4, 27, 28, 32, 33, 34, 35, 36, 37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.expressionStmt()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.compoundStmt()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 112
                self.selectionStmt()
                pass
            elif token in [13, 14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 113
                self.iterationStmt()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 5)
                self.state = 114
                self.returnStmt()
                pass
            elif token in [16, 17]:
                self.enterOuterAlt(localctx, 6)
                self.state = 115
                self.ioStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_expressionStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStmt" ):
                listener.enterExpressionStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStmt" ):
                listener.exitExpressionStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStmt" ):
                return visitor.visitExpressionStmt(self)
            else:
                return visitor.visitChildren(self)




    def expressionStmt(self):

        localctx = MiniCParser.ExpressionStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expressionStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 270985592834) != 0):
                self.state = 118
                self.expression()


            self.state = 121
            self.match(MiniCParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectionStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniCParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_selectionStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectionStmt" ):
                listener.enterSelectionStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectionStmt" ):
                listener.exitSelectionStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectionStmt" ):
                return visitor.visitSelectionStmt(self)
            else:
                return visitor.visitChildren(self)




    def selectionStmt(self):

        localctx = MiniCParser.SelectionStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_selectionStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(MiniCParser.T__10)
            self.state = 124
            self.match(MiniCParser.T__0)
            self.state = 125
            self.expression()
            self.state = 126
            self.match(MiniCParser.T__1)
            self.state = 127
            self.statement()
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 128
                self.match(MiniCParser.T__11)
                self.state = 129
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterationStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.ExpressionContext,i)


        def statement(self):
            return self.getTypedRuleContext(MiniCParser.StatementContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_iterationStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterationStmt" ):
                listener.enterIterationStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterationStmt" ):
                listener.exitIterationStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterationStmt" ):
                return visitor.visitIterationStmt(self)
            else:
                return visitor.visitChildren(self)




    def iterationStmt(self):

        localctx = MiniCParser.IterationStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_iterationStmt)
        self._la = 0 # Token type
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(MiniCParser.T__12)
                self.state = 133
                self.match(MiniCParser.T__0)
                self.state = 134
                self.expression()
                self.state = 135
                self.match(MiniCParser.T__1)
                self.state = 136
                self.statement()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(MiniCParser.T__13)
                self.state = 139
                self.match(MiniCParser.T__0)
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 270985592834) != 0):
                    self.state = 140
                    self.expression()


                self.state = 143
                self.match(MiniCParser.T__3)
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 270985592834) != 0):
                    self.state = 144
                    self.expression()


                self.state = 147
                self.match(MiniCParser.T__3)
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 270985592834) != 0):
                    self.state = 148
                    self.expression()


                self.state = 151
                self.match(MiniCParser.T__1)
                self.state = 152
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = MiniCParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(MiniCParser.T__14)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 270985592834) != 0):
                self.state = 156
                self.expression()


            self.state = 159
            self.match(MiniCParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IoStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MiniCParser.STRING, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.ExpressionContext,i)


        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.IDENTIFIER)
            else:
                return self.getToken(MiniCParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return MiniCParser.RULE_ioStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIoStmt" ):
                listener.enterIoStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIoStmt" ):
                listener.exitIoStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIoStmt" ):
                return visitor.visitIoStmt(self)
            else:
                return visitor.visitChildren(self)




    def ioStmt(self):

        localctx = MiniCParser.IoStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ioStmt)
        self._la = 0 # Token type
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.match(MiniCParser.T__15)
                self.state = 162
                self.match(MiniCParser.T__0)
                self.state = 163
                self.match(MiniCParser.STRING)
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 164
                    self.match(MiniCParser.T__2)
                    self.state = 165
                    self.expression()
                    self.state = 170
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 171
                self.match(MiniCParser.T__1)
                self.state = 172
                self.match(MiniCParser.T__3)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(MiniCParser.T__16)
                self.state = 174
                self.match(MiniCParser.T__0)
                self.state = 175
                self.match(MiniCParser.STRING)
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 176
                    self.match(MiniCParser.T__2)
                    self.state = 178
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==18:
                        self.state = 177
                        self.match(MiniCParser.T__17)


                    self.state = 180
                    self.match(MiniCParser.IDENTIFIER)
                    self.state = 185
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 186
                self.match(MiniCParser.T__1)
                self.state = 187
                self.match(MiniCParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentExpr(self):
            return self.getTypedRuleContext(MiniCParser.AssignmentExprContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MiniCParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.assignmentExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOrExpr(self):
            return self.getTypedRuleContext(MiniCParser.LogicalOrExprContext,0)


        def assignmentExpr(self):
            return self.getTypedRuleContext(MiniCParser.AssignmentExprContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_assignmentExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentExpr" ):
                listener.enterAssignmentExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentExpr" ):
                listener.exitAssignmentExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentExpr" ):
                return visitor.visitAssignmentExpr(self)
            else:
                return visitor.visitChildren(self)




    def assignmentExpr(self):

        localctx = MiniCParser.AssignmentExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assignmentExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.logicalOrExpr()
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 193
                self.match(MiniCParser.T__4)
                self.state = 194
                self.assignmentExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.LogicalAndExprContext)
            else:
                return self.getTypedRuleContext(MiniCParser.LogicalAndExprContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_logicalOrExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOrExpr" ):
                listener.enterLogicalOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOrExpr" ):
                listener.exitLogicalOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrExpr" ):
                return visitor.visitLogicalOrExpr(self)
            else:
                return visitor.visitChildren(self)




    def logicalOrExpr(self):

        localctx = MiniCParser.LogicalOrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_logicalOrExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.logicalAndExpr()
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 198
                self.match(MiniCParser.T__18)
                self.state = 199
                self.logicalAndExpr()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.EqualityExprContext)
            else:
                return self.getTypedRuleContext(MiniCParser.EqualityExprContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_logicalAndExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAndExpr" ):
                listener.enterLogicalAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAndExpr" ):
                listener.exitLogicalAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndExpr" ):
                return visitor.visitLogicalAndExpr(self)
            else:
                return visitor.visitChildren(self)




    def logicalAndExpr(self):

        localctx = MiniCParser.LogicalAndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_logicalAndExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.equalityExpr()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 206
                self.match(MiniCParser.T__19)
                self.state = 207
                self.equalityExpr()
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.RelationalExprContext)
            else:
                return self.getTypedRuleContext(MiniCParser.RelationalExprContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_equalityExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpr" ):
                listener.enterEqualityExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpr" ):
                listener.exitEqualityExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpr" ):
                return visitor.visitEqualityExpr(self)
            else:
                return visitor.visitChildren(self)




    def equalityExpr(self):

        localctx = MiniCParser.EqualityExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_equalityExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.relationalExpr()
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21 or _la==22:
                self.state = 214
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 215
                self.relationalExpr()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.AdditiveExprContext)
            else:
                return self.getTypedRuleContext(MiniCParser.AdditiveExprContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_relationalExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpr" ):
                listener.enterRelationalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpr" ):
                listener.exitRelationalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpr" ):
                return visitor.visitRelationalExpr(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpr(self):

        localctx = MiniCParser.RelationalExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_relationalExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.additiveExpr()
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0):
                self.state = 222
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 223
                self.additiveExpr()
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.MultiplicativeExprContext)
            else:
                return self.getTypedRuleContext(MiniCParser.MultiplicativeExprContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_additiveExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpr" ):
                listener.enterAdditiveExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpr" ):
                listener.exitAdditiveExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpr" ):
                return visitor.visitAdditiveExpr(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpr(self):

        localctx = MiniCParser.AdditiveExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_additiveExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.multiplicativeExpr()
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27 or _la==28:
                self.state = 230
                _la = self._input.LA(1)
                if not(_la==27 or _la==28):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 231
                self.multiplicativeExpr()
                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.UnaryExprContext)
            else:
                return self.getTypedRuleContext(MiniCParser.UnaryExprContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_multiplicativeExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpr" ):
                listener.enterMultiplicativeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpr" ):
                listener.exitMultiplicativeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpr" ):
                return visitor.visitMultiplicativeExpr(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpr(self):

        localctx = MiniCParser.MultiplicativeExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_multiplicativeExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.unaryExpr()
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0):
                self.state = 238
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 239
                self.unaryExpr()
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self):
            return self.getTypedRuleContext(MiniCParser.UnaryExprContext,0)


        def primaryExpr(self):
            return self.getTypedRuleContext(MiniCParser.PrimaryExprContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_unaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpr" ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpr" ):
                listener.exitUnaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = MiniCParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_unaryExpr)
        self._la = 0 # Token type
        try:
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27, 28, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4697620480) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 246
                self.unaryExpr()
                pass
            elif token in [1, 33, 34, 35, 36, 37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.primaryExpr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniCParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(MiniCParser.NUMBER, 0)

        def CHAR(self):
            return self.getToken(MiniCParser.CHAR, 0)

        def BOOL(self):
            return self.getToken(MiniCParser.BOOL, 0)

        def STRING(self):
            return self.getToken(MiniCParser.STRING, 0)

        def argumentList(self):
            return self.getTypedRuleContext(MiniCParser.ArgumentListContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_primaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpr" ):
                listener.enterPrimaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpr" ):
                listener.exitPrimaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpr" ):
                return visitor.visitPrimaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpr(self):

        localctx = MiniCParser.PrimaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_primaryExpr)
        self._la = 0 # Token type
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.match(MiniCParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.match(MiniCParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.match(MiniCParser.CHAR)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 253
                self.match(MiniCParser.BOOL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 254
                self.match(MiniCParser.STRING)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 255
                self.match(MiniCParser.IDENTIFIER)
                self.state = 256
                self.match(MiniCParser.T__0)
                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 270985592834) != 0):
                    self.state = 257
                    self.argumentList()


                self.state = 260
                self.match(MiniCParser.T__1)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 261
                self.match(MiniCParser.T__0)
                self.state = 262
                self.expression()
                self.state = 263
                self.match(MiniCParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = MiniCParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.expression()
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 268
                self.match(MiniCParser.T__2)
                self.state = 269
                self.expression()
                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





