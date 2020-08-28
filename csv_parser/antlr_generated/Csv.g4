grammar Csv;

// parser rules

csv: line+ EOF;

line: ( cell? SEPARATOR )+ cell? NEWLINE?;   

cell: WHITESPACE? field? WHITESPACE?;

field: (INTEGER | FLOAT | STRING);

// lexer rules

fragment DIGIT: [0-9];

INTEGER: DIGIT+; 

FLOAT: DIGIT '.' DIGIT+;

STRING: ('"' | '\'') (' ' | [a-z] | [A-Z])* ('"' | '\'');

NEWLINE: ('\n' | '\r')+;

SEPARATOR: ',';

WHITESPACE: (' ' | '\t')+;