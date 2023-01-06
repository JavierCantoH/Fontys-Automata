grammar MyGrammar2;

// rules
program : command+ ;

command : declare_fun | assert_cmd | check_sat | get_model ;

declare_fun : '(' 'declare-fun' ID '()' 'Int' ')' ;

assert_cmd : '(' 'assert' formula ')';

distinct_formula : '(' 'distinct' values values values*')' ;

values: (ID | NUMBER);

formula : distinct_formula
        | '(' comp formula formula ')'
        | '(' comparator values values ')'
        | values
        ;

comparator : '>=' | '<=' | '<' | '>' | '=';

comp: 'and' | 'or';

check_sat : '(' 'check-sat' ')';

get_model : '(' 'get-model' ')';

COMMENT : ';' .*? '\n' -> skip ;

// tokens
ID : [a-zA-Z]+[a-zA-Z0-9]* ;
NUMBER : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;