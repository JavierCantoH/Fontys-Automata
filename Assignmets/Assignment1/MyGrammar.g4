grammar MyGrammar;

// rules
expr:	left=expr op=('*'|'/') right=expr  # OpExpr
    |	left=expr op=('+'|'-') right=expr  # OpExpr
    |	atom=NUMBER                        # AtomExpr
    |	'(' expr ')'                       # ParenExpr
    ;

// tokens
NUMBER: [0-9]+ ;
WS: [ \t]+ -> skip ; // skip spaces
