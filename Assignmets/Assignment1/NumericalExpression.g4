grammar NumericalExpression;

//rules

numericalExpression
  : variableAssignment
  | printStatement
  | mathematicalExpression
  ;

variableAssignment
  : VariableName '=' mathematicalExpression
  ;

printStatement
  : 'print' VariableName
  ;

mathematicalExpression
  : Number
  | VariableName
  | mathematicalExpression operator mathematicalExpression
  | '(' mathematicalExpression ')'
  ;

operator
  : '+'
  | '-'
  | '*'
  | '/'
  ;

// tokens

VariableName:('a'..'z'|'A'..'Z')+ ;

Number: [0-9]+ ;

WS: (' '|'\n'|'\t')+ -> skip;