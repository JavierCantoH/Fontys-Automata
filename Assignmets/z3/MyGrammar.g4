grammar MyGrammar;
// TODO comments

// rules
prog: statement*;

statement:    declaration 
            | checksat 
            | getmodel 
            | assertion
            ;

// (declare-fun a11 () Int)
declaration: OPENPARENS DECLAREFUN ID OPENPARENS CLOSINGPARENS INT CLOSINGPARENS;
            
// (check-sat)
checksat: OPENPARENS CHECKSATWORD CLOSINGPARENS;

// (get-model)
getmodel: OPENPARENS GETMODELWORD CLOSINGPARENS;

// (assert constraint)
assertion: OPENPARENS ASSERTWORD constraint CLOSINGPARENS;

constraint:     OPENPARENS DISTINCT (ID)+ CLOSINGPARENS // (distinct _ _ _)
            |   OPENPARENS AND constraint constraint CLOSINGPARENS // (and (x)(x))
            |   OPENPARENS OR constraint constraint CLOSINGPARENS // (or (x)(x))
            |   OPENPARENS GREATER (ID | NUMBER) (ID | NUMBER) CLOSINGPARENS // (> _ _)
            |   OPENPARENS LESS (ID | NUMBER) (ID | NUMBER) CLOSINGPARENS // (< _ _)
            |   OPENPARENS GREATER_EQUAL (ID | NUMBER) (ID | NUMBER) CLOSINGPARENS // (>= _ _)
            |   OPENPARENS LESS_EQUAL (ID | NUMBER) (ID | NUMBER) CLOSINGPARENS // (<= _ _)
            |   OPENPARENS BOOLEAN_EQUAL (ID | NUMBER) (ID | NUMBER) CLOSINGPARENS // (= _ _)
            ;


// tokens
SEMICOLON: ';';
GREATER: '>';
LESS: '<';
GREATER_EQUAL: '>=';
LESS_EQUAL: '<=';
BOOLEAN_EQUAL: '=';
AND: 'and';
OR: 'or';
OPENPARENS: '(';
CLOSINGPARENS: ')';
DECLAREFUN: 'declare-fun';
INT: 'Int';
ID : [a-zA-Z_][a-zA-Z_0-9-]*;
NUMBER: [0-9]+;
ASSERTWORD: 'assert';
DISTINCT: 'distinct';
CHECKSATWORD: 'check-sat';
GETMODELWORD: 'get-model';
WS : [ \t\r\n]+ -> skip;