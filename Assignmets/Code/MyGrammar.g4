grammar MyGrammar;

//rules

prog: statement+;

statement:  expr NEWLINE          # printLine // code in main
         |  ID EQUAL expr NEWLINE # assign // code in main
         |  NEWLINE               # blank
         |  print                 # printExpr 
         |  ifStat                # ifExpr
         |  loop                  # loopExpr
         ;

expr:   left=expr op=(MUL|DIV) right=expr  # operation // code in main
    |	left=expr op=(PLUS|MIN) right=expr # operation // code in main
    |   left=expr op=(AND|OR) right=expr   # operation // code in main
    |	INT                                # int // code in main
    |   ID				                   # id // code in main
    |	OPENPARENS expr CLOSINGPARENS      # parens // code in main
    |   TEXT				               # text // code in main
    ;

print: PRINT expr; // code in main

loop: WHILE expr DO statement; // code in main

ifStat: IF expr THEN statement;  // ( ELSE statement )? FI code in main

// TODO (optional!) declare variables without assginment

// tokens
TEXT: '"' ~('\r' | '\n' | '"')* '"';
WHILE: 'while';
DO: 'do';
AND: 'and';
OR: 'or';
IF: 'if';
THEN: 'then';
ELSE: 'else';
FI: 'fi';
PRINT: 'print';
EQUAL: '=';
INT: [0-9]+;
NEWLINE:'\r'? '\n';
ID: [a-zA-Z]+; 
MUL: '*';
DIV: '/';
PLUS: '+';
MIN: '-';
OPENPARENS: '(';
CLOSINGPARENS: ')';
WS: [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines