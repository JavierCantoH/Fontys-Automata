
grammar MyGrammar;

// rules
myStart: expr EOF; 
expr : '-' expr
     | expr ('*'|'/') expr
     | expr ('+'|'-') expr
     | '(' expr ')'
     | NUM
;
num: NUM;
//WS: (' '|'\n'|'\t')+ -> skip;
WS: [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

// tokens
NUM: [0-9]+; 