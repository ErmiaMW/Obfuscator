grammar MiniC;

program         : (functionDecl | declaration)* EOF ;

functionDecl    : typeSpecifier IDENTIFIER '(' params? ')' compoundStmt ;

params          : param (',' param)* ;
param           : typeSpecifier IDENTIFIER ;

declaration     : typeSpecifier initDeclaratorList ';' ;
initDeclaratorList : initDeclarator (',' initDeclarator)* ;
initDeclarator  : IDENTIFIER ('=' expression)? ;

typeSpecifier   : 'int' | 'char' | 'bool' ;

compoundStmt    : '{' (declaration | statement)* '}' ;

statement
    : expressionStmt
    | compoundStmt
    | selectionStmt
    | iterationStmt
    | returnStmt
    | ioStmt ;

expressionStmt  : expression? ';' ;

selectionStmt   : 'if' '(' expression ')' statement ('else' statement)? ;

iterationStmt   : 'while' '(' expression ')' statement
                | 'for' '(' expression? ';' expression? ';' expression? ')' statement ;

returnStmt      : 'return' expression? ';' ;

ioStmt          : 'printf' '(' STRING (',' expression)* ')' ';'
                | 'scanf' '(' STRING (',' '&'? IDENTIFIER)* ')' ';' ;

expression
    : assignmentExpr ;

assignmentExpr
    : logicalOrExpr ('=' assignmentExpr)? ;

logicalOrExpr
    : logicalAndExpr ('||' logicalAndExpr)* ;

logicalAndExpr
    : equalityExpr ('&&' equalityExpr)* ;

equalityExpr
    : relationalExpr (('==' | '!=') relationalExpr)* ;

relationalExpr
    : additiveExpr (('<' | '<=' | '>' | '>=') additiveExpr)* ;

additiveExpr
    : multiplicativeExpr (('+' | '-') multiplicativeExpr)* ;

multiplicativeExpr
    : unaryExpr (('*' | '/' | '%') unaryExpr)* ;

unaryExpr
    : ('+' | '-' | '!') unaryExpr
    | primaryExpr ;

primaryExpr
    : IDENTIFIER
    | NUMBER
    | CHAR
    | BOOL
    | STRING
    | IDENTIFIER '(' argumentList? ')'   // function call
    | '(' expression ')' ;

argumentList
    : expression (',' expression)* ;

// ----------------------- LEXER RULES -----------------------

BOOL        : 'true' | 'false' ;
CHAR        : '\'' . '\'' ;
STRING      : '"' (~["\\] | '\\' .)* '"' ;

NUMBER      : [0-9]+ ;
IDENTIFIER  : [a-zA-Z_][a-zA-Z0-9_]* ;

WS          : [ \t\r\n]+ -> channel(HIDDEN) ;
LINE_COMMENT: '//' ~[\r\n]* -> channel(HIDDEN) ;
BLOCK_COMMENT: '/*' .*? '*/' -> channel(HIDDEN) ;

