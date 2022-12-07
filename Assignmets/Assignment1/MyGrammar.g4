grammar MyGrammar;

//rules

prog: (decl | expr)+ EOF # Program;

decl: ID '=' NUM # Declaration;

expr:	left=expr op=('*'|'/') right=expr  # OperationExpr
    |	left=expr op=('+'|'-') right=expr  # OperationExpr
    |	num=NUM                            # Number
    |   id=ID                              # Variable 
    |	'(' expr ')'                       # ParentExpr
    ;

// tokens
NUM: [0-9]+ ;
ID: ('a'..'z'|'A'..'Z')+ ;
// WS: [ \t]+ -> skip ; // skip spaces
WS: (' '|'\n'|'\t')+ -> skip; // skip spaces, tabs and new lines
//WS: ('\n'|'\t')+ -> skip; // tabs and new lines
INT_TYPE: 'INT';