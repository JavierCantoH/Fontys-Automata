grammar NumericalExpression;

//rules

prog: statement+;

statement:  expr NEWLINE          # print
         |  ID EQUAL expr NEWLINE # assign
         |  NEWLINE               # blank
         ;

expr:   left=expr op=(MUL|DIV) right=expr  # operation
    |	left=expr op=(PLUS|MIN) right=expr # operation
    |	INT                                # int
    |   ID				                   # id
    |	OPENPARENS expr CLOSINGPARENS      # parens
    ;

// TODO print function
// TODO declare variables without assginment

// tokens
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