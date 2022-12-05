grammar MyGrammar;

// rules
expr:	left=expr op=('*'|'/') right=expr  # OperationExpr
    |	left=expr op=('+'|'-') right=expr  # OperationExpr
    |	num=NUMBER                         # NumberExpr
    |	'(' expr ')'                       # ParentExpr
    ;

// tokens
NUMBER: [0-9]+ ;
WS: [ \t]+ -> skip ; // skip spaces
