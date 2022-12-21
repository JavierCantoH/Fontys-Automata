grammar MyGrammar;

//rules

prog: statement+;

statement:  expr NEWLINE                        # printLine // code in main
         |  TYPE ID ( EQUAL expr )? SEMICOLON   # assign // code in main
         |  ID EQUAL expr SEMICOLON             # assignExpr // code in main
         |  NEWLINE                             # blank
         |  print                               # printExpr 
         |  ifStat                              # ifExpr
         |  loop                                # loopExpr
         ;

expr:   left=expr op=(MUL|DIV) right=expr                           # operation // code in main
    |	left=expr op=(PLUS|MIN) right=expr                          # operation // code in main
    |   left=expr op=(AND|OR) right=expr                            # operation // code in main
    |   left=expr op=(GREATER|LESS) right=expr                      # operation // code in main
    |   left=expr op=(GREATER_EQUAL|LESS_EQUAL) right=expr          # operation // code in main
    |   left=expr op=(BOOLEAN_EQUAL|BOOLEAN_NOT_EQUAL) right=expr   # operation // code in main
    |	( INT | FLOAT )                                             # number // code in main
    |   ID				                                            # id // code in main
    |	OPENPARENS expr CLOSINGPARENS                               # parens // code in main
    |   TEXT				                                        # text // code in main
    ;

print: PRINT expr; // code in main

loop: WHILE expr DO statement; // code in main

ifStat: IF expr THEN statement ( ELSE statement )?;  // code in main

// tokens
TYPE: 'float' | 'int' | 'void' ;
SEMICOLON: ';';
GREATER: '>';
LESS: '<';
GREATER_EQUAL: '>=';
LESS_EQUAL: '<=';
BOOLEAN_EQUAL: '==';
BOOLEAN_NOT_EQUAL: '!=';
TEXT: '"' ~('\r' | '\n' | '"')* '"';
WHILE: 'while';
DO: 'do';
AND: 'and';
OR: 'or';
IF: 'if';
THEN: 'then';
ELSE: 'else';
PRINT: 'print';
EQUAL: '=';
INT: [0-9]+;
FLOAT  : '-'? INT '.' INT ;
NEWLINE:'\r'? '\n';
ID: [a-zA-Z]+; 
MUL: '*';
DIV: '/';
PLUS: '+';
MIN: '-';
OPENPARENS: '(';
CLOSINGPARENS: ')';
WS: [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines