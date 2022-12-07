grammar MyGrammar;

// rules
expr returns [int value]
    :	left=expr op=('*'|'/') right=expr  # OperationExpr
    |	left=expr op=('+'|'-') right=expr  # OperationExpr
    |	num=NUMBER                         # NumberExpr
    |	'(' expr ')'                       # ParentExpr
    |   left=CHAR op='=' right=expr        # VariableAssignExpr
    |   CHAR                               # VariableExpr
    ;



// tokens
NUMBER: [0-9]+ ;
CHAR: ('a'..'z'|'A'..'Z')+ ;
// WS: [ \t]+ -> skip ; // skip spaces
WS : (' '|'\n'|'\t')+ -> skip; // skip spaces, tabs and new lines
