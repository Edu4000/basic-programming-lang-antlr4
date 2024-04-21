grammar Act_31;

prog: (line | func_struct)*;

line: declaration | definition ';';

type: INT | FLOAT | STRING;

declaration: type tk_ID;

definition: declaration '=' value | tk_ID '=' value;

value:
	tk_int
	| tk_float
	| tk_string
	| tk_string
	| op
	| func_call;

func_call: tk_ID '()' | tk_ID '(' value (',' value)* ')';

// Operations
op:
	op '+' op			# sum
	| op '-' op			# sub
	| op '*' op			# mult
	| op '/' op			# div
	| op '^' op			# pow
	| 'sqrt(' op ')'	# sqrt
	| variable			# varOp
	| '(' op ')'		# par;

variable:
	tk_int		# int
	| tk_float	# float
	| tk_string	# string
	| tk_ID		# var;

// Boolean Operations
boolean:
	boolean '&&' boolean
	| boolean '||' boolean
	| boolean '^' boolean
	| '!' boolean
	| TRUE
	| FALSE
	| compare;

compare:
	variable '<' variable
	| variable '>' variable
	| variable '==' variable
	| variable '>=' variable
	| variable '<=' variable
	| '(' compare ')';

// Structure IF
if_struct: if else_if* else | if else_if*;
if: 'if' '(' boolean ')' '{' line+ '}';
else_if: 'else' 'if' '(' boolean ')' '{' line+ '}';
else: 'else' '{' line+ '}';

// Structure while
while_struct: 'while' '(' boolean ')' '{' line+ '}';

// Function Structure
func_struct: func func_body;

func_type: type | VOID;

func:
	func_type tk_ID '(' declaration (',' declaration)* ')'
	| func_type tk_ID '(' ')';

func_body: '{' line* return '}' | '{' line* '}';

return: 'return' variable ';';

// Tokens
tk_main: 'main';
INT: 'int';
FLOAT: 'float';
STRING: 'string';
VOID: 'void';
TRUE: 'TRUE';
FALSE: 'FALSE';
tk_ID: ID;
tk_int: DEC* NUM+;
tk_float: DEC* NUM+ '.' NUM+;
tk_string: STR;
tk_add: '+';
tk_sub: '-';
tk_mult: '*';

// Lexer Rules

ID: [a-zA-Z][a-zA-Z0-9_]*; // identifiers	# ID
NUM: [0-9]; // numbers
DEC: [1-9];
STR: ['][a-zA-Z0-9,. ]* ['];
WS:
	[ \t\r\n]+ -> skip; // skip spaces, tabs, newlines-> skip; // skip spaces, tabs, newlines