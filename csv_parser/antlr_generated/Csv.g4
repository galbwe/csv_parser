grammar Csv;

// parser rules

csv: line+ EOF;

line: ( cell? SEPARATOR )+ cell? NEWLINE?;   

cell: WHITESPACE? field? WHITESPACE?;

field: (INTEGER | FLOAT);

// lexer rules

fragment DIGIT: [0-9];

INTEGER: DIGIT+; 

FLOAT: DIGIT '.' DIGIT+;

NEWLINE: ('\n' | '\r')+;

SEPARATOR: ',';

WHITESPACE: (' ' | '\t')+;