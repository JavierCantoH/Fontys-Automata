grammar MyGrammar;

//rules

prog: statement+;

statement:  expr NEWLINE          # printLine
         |  ID EQUAL expr NEWLINE # assign
         |  NEWLINE               # blank
         |  print                 # printExpr
         ;

expr:   left=expr op=(MUL|DIV) right=expr  # operation
    |	left=expr op=(PLUS|MIN) right=expr # operation
    |	INT                                # int
    |   ID				                   # id
    |	OPENPARENS expr CLOSINGPARENS      # parens
    ;

print: PRINT expr;

// TODO OPTIONAL! declare variables without assginment

// tokens
PRINT: 'print';
COMMA: ',';
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
WS : [ \t]+ -> skip;