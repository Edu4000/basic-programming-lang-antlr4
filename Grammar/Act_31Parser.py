# Generated from ./Grammar/Act_31.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,39,352,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,1,0,5,0,61,8,0,10,0,12,0,64,9,0,1,1,1,1,
        1,1,1,1,3,1,70,8,1,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,3,4,85,8,4,1,5,1,5,1,5,1,5,1,5,3,5,92,8,5,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,5,6,102,8,6,10,6,12,6,105,9,6,1,6,1,6,3,6,109,8,
        6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,121,8,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,138,8,7,10,
        7,12,7,141,9,7,1,8,1,8,1,8,1,8,3,8,147,8,8,1,9,1,9,1,9,1,9,1,9,1,
        9,3,9,155,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,166,8,9,10,
        9,12,9,169,9,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,3,10,195,8,10,1,11,1,11,5,11,199,8,11,10,11,12,11,202,9,11,
        1,11,1,11,1,11,1,11,5,11,208,8,11,10,11,12,11,211,9,11,3,11,213,
        8,11,1,12,1,12,1,12,1,12,1,12,1,12,4,12,221,8,12,11,12,12,12,222,
        1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,4,13,234,8,13,11,13,
        12,13,235,1,13,1,13,1,14,1,14,1,14,4,14,243,8,14,11,14,12,14,244,
        1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,4,15,255,8,15,11,15,12,15,
        256,1,15,1,15,1,16,1,16,1,16,1,17,1,17,3,17,266,8,17,1,18,1,18,1,
        18,1,18,1,18,1,18,5,18,274,8,18,10,18,12,18,277,9,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,3,18,286,8,18,1,19,1,19,5,19,290,8,19,10,
        19,12,19,293,9,19,1,19,1,19,1,19,1,19,1,19,5,19,300,8,19,10,19,12,
        19,303,9,19,1,19,3,19,306,8,19,1,20,1,20,1,20,1,20,1,21,1,21,1,22,
        1,22,1,23,5,23,317,8,23,10,23,12,23,320,9,23,1,23,4,23,323,8,23,
        11,23,12,23,324,1,24,5,24,328,8,24,10,24,12,24,331,9,24,1,24,4,24,
        334,8,24,11,24,12,24,335,1,24,1,24,4,24,340,8,24,11,24,12,24,341,
        1,25,1,25,1,26,1,26,1,27,1,27,1,28,1,28,1,28,0,2,14,18,29,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,0,1,1,0,29,31,371,0,62,1,0,0,0,2,69,1,0,0,0,4,71,1,0,
        0,0,6,73,1,0,0,0,8,84,1,0,0,0,10,91,1,0,0,0,12,108,1,0,0,0,14,120,
        1,0,0,0,16,146,1,0,0,0,18,154,1,0,0,0,20,194,1,0,0,0,22,212,1,0,
        0,0,24,214,1,0,0,0,26,226,1,0,0,0,28,239,1,0,0,0,30,248,1,0,0,0,
        32,260,1,0,0,0,34,265,1,0,0,0,36,285,1,0,0,0,38,305,1,0,0,0,40,307,
        1,0,0,0,42,311,1,0,0,0,44,313,1,0,0,0,46,318,1,0,0,0,48,329,1,0,
        0,0,50,343,1,0,0,0,52,345,1,0,0,0,54,347,1,0,0,0,56,349,1,0,0,0,
        58,61,3,2,1,0,59,61,3,32,16,0,60,58,1,0,0,0,60,59,1,0,0,0,61,64,
        1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,1,1,0,0,0,64,62,1,0,0,0,65,
        70,3,6,3,0,66,67,3,8,4,0,67,68,5,1,0,0,68,70,1,0,0,0,69,65,1,0,0,
        0,69,66,1,0,0,0,70,3,1,0,0,0,71,72,7,0,0,0,72,5,1,0,0,0,73,74,3,
        4,2,0,74,75,3,44,22,0,75,7,1,0,0,0,76,77,3,6,3,0,77,78,5,2,0,0,78,
        79,3,10,5,0,79,85,1,0,0,0,80,81,3,44,22,0,81,82,5,2,0,0,82,83,3,
        10,5,0,83,85,1,0,0,0,84,76,1,0,0,0,84,80,1,0,0,0,85,9,1,0,0,0,86,
        92,3,46,23,0,87,92,3,48,24,0,88,92,3,50,25,0,89,92,3,14,7,0,90,92,
        3,12,6,0,91,86,1,0,0,0,91,87,1,0,0,0,91,88,1,0,0,0,91,89,1,0,0,0,
        91,90,1,0,0,0,92,11,1,0,0,0,93,94,3,44,22,0,94,95,5,3,0,0,95,109,
        1,0,0,0,96,97,3,44,22,0,97,98,5,4,0,0,98,103,3,10,5,0,99,100,5,5,
        0,0,100,102,3,10,5,0,101,99,1,0,0,0,102,105,1,0,0,0,103,101,1,0,
        0,0,103,104,1,0,0,0,104,106,1,0,0,0,105,103,1,0,0,0,106,107,5,6,
        0,0,107,109,1,0,0,0,108,93,1,0,0,0,108,96,1,0,0,0,109,13,1,0,0,0,
        110,111,6,7,-1,0,111,112,5,12,0,0,112,113,3,14,7,0,113,114,5,6,0,
        0,114,121,1,0,0,0,115,121,3,16,8,0,116,117,5,4,0,0,117,118,3,14,
        7,0,118,119,5,6,0,0,119,121,1,0,0,0,120,110,1,0,0,0,120,115,1,0,
        0,0,120,116,1,0,0,0,121,139,1,0,0,0,122,123,10,8,0,0,123,124,5,7,
        0,0,124,138,3,14,7,9,125,126,10,7,0,0,126,127,5,8,0,0,127,138,3,
        14,7,8,128,129,10,6,0,0,129,130,5,9,0,0,130,138,3,14,7,7,131,132,
        10,5,0,0,132,133,5,10,0,0,133,138,3,14,7,6,134,135,10,4,0,0,135,
        136,5,11,0,0,136,138,3,14,7,5,137,122,1,0,0,0,137,125,1,0,0,0,137,
        128,1,0,0,0,137,131,1,0,0,0,137,134,1,0,0,0,138,141,1,0,0,0,139,
        137,1,0,0,0,139,140,1,0,0,0,140,15,1,0,0,0,141,139,1,0,0,0,142,147,
        3,46,23,0,143,147,3,48,24,0,144,147,3,50,25,0,145,147,3,44,22,0,
        146,142,1,0,0,0,146,143,1,0,0,0,146,144,1,0,0,0,146,145,1,0,0,0,
        147,17,1,0,0,0,148,149,6,9,-1,0,149,150,5,15,0,0,150,155,3,18,9,
        4,151,155,5,33,0,0,152,155,5,34,0,0,153,155,3,20,10,0,154,148,1,
        0,0,0,154,151,1,0,0,0,154,152,1,0,0,0,154,153,1,0,0,0,155,167,1,
        0,0,0,156,157,10,7,0,0,157,158,5,13,0,0,158,166,3,18,9,8,159,160,
        10,6,0,0,160,161,5,14,0,0,161,166,3,18,9,7,162,163,10,5,0,0,163,
        164,5,11,0,0,164,166,3,18,9,6,165,156,1,0,0,0,165,159,1,0,0,0,165,
        162,1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,168,
        19,1,0,0,0,169,167,1,0,0,0,170,171,3,16,8,0,171,172,5,16,0,0,172,
        173,3,16,8,0,173,195,1,0,0,0,174,175,3,16,8,0,175,176,5,17,0,0,176,
        177,3,16,8,0,177,195,1,0,0,0,178,179,3,16,8,0,179,180,5,18,0,0,180,
        181,3,16,8,0,181,195,1,0,0,0,182,183,3,16,8,0,183,184,5,19,0,0,184,
        185,3,16,8,0,185,195,1,0,0,0,186,187,3,16,8,0,187,188,5,20,0,0,188,
        189,3,16,8,0,189,195,1,0,0,0,190,191,5,4,0,0,191,192,3,20,10,0,192,
        193,5,6,0,0,193,195,1,0,0,0,194,170,1,0,0,0,194,174,1,0,0,0,194,
        178,1,0,0,0,194,182,1,0,0,0,194,186,1,0,0,0,194,190,1,0,0,0,195,
        21,1,0,0,0,196,200,3,24,12,0,197,199,3,26,13,0,198,197,1,0,0,0,199,
        202,1,0,0,0,200,198,1,0,0,0,200,201,1,0,0,0,201,203,1,0,0,0,202,
        200,1,0,0,0,203,204,3,28,14,0,204,213,1,0,0,0,205,209,3,24,12,0,
        206,208,3,26,13,0,207,206,1,0,0,0,208,211,1,0,0,0,209,207,1,0,0,
        0,209,210,1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,212,196,1,0,0,
        0,212,205,1,0,0,0,213,23,1,0,0,0,214,215,5,21,0,0,215,216,5,4,0,
        0,216,217,3,18,9,0,217,218,5,6,0,0,218,220,5,22,0,0,219,221,3,2,
        1,0,220,219,1,0,0,0,221,222,1,0,0,0,222,220,1,0,0,0,222,223,1,0,
        0,0,223,224,1,0,0,0,224,225,5,23,0,0,225,25,1,0,0,0,226,227,5,24,
        0,0,227,228,5,21,0,0,228,229,5,4,0,0,229,230,3,18,9,0,230,231,5,
        6,0,0,231,233,5,22,0,0,232,234,3,2,1,0,233,232,1,0,0,0,234,235,1,
        0,0,0,235,233,1,0,0,0,235,236,1,0,0,0,236,237,1,0,0,0,237,238,5,
        23,0,0,238,27,1,0,0,0,239,240,5,24,0,0,240,242,5,22,0,0,241,243,
        3,2,1,0,242,241,1,0,0,0,243,244,1,0,0,0,244,242,1,0,0,0,244,245,
        1,0,0,0,245,246,1,0,0,0,246,247,5,23,0,0,247,29,1,0,0,0,248,249,
        5,25,0,0,249,250,5,4,0,0,250,251,3,18,9,0,251,252,5,6,0,0,252,254,
        5,22,0,0,253,255,3,2,1,0,254,253,1,0,0,0,255,256,1,0,0,0,256,254,
        1,0,0,0,256,257,1,0,0,0,257,258,1,0,0,0,258,259,5,23,0,0,259,31,
        1,0,0,0,260,261,3,36,18,0,261,262,3,38,19,0,262,33,1,0,0,0,263,266,
        3,4,2,0,264,266,5,32,0,0,265,263,1,0,0,0,265,264,1,0,0,0,266,35,
        1,0,0,0,267,268,3,34,17,0,268,269,3,44,22,0,269,270,5,4,0,0,270,
        275,3,6,3,0,271,272,5,5,0,0,272,274,3,6,3,0,273,271,1,0,0,0,274,
        277,1,0,0,0,275,273,1,0,0,0,275,276,1,0,0,0,276,278,1,0,0,0,277,
        275,1,0,0,0,278,279,5,6,0,0,279,286,1,0,0,0,280,281,3,34,17,0,281,
        282,3,44,22,0,282,283,5,4,0,0,283,284,5,6,0,0,284,286,1,0,0,0,285,
        267,1,0,0,0,285,280,1,0,0,0,286,37,1,0,0,0,287,291,5,22,0,0,288,
        290,3,2,1,0,289,288,1,0,0,0,290,293,1,0,0,0,291,289,1,0,0,0,291,
        292,1,0,0,0,292,294,1,0,0,0,293,291,1,0,0,0,294,295,3,40,20,0,295,
        296,5,23,0,0,296,306,1,0,0,0,297,301,5,22,0,0,298,300,3,2,1,0,299,
        298,1,0,0,0,300,303,1,0,0,0,301,299,1,0,0,0,301,302,1,0,0,0,302,
        304,1,0,0,0,303,301,1,0,0,0,304,306,5,23,0,0,305,287,1,0,0,0,305,
        297,1,0,0,0,306,39,1,0,0,0,307,308,5,26,0,0,308,309,3,16,8,0,309,
        310,5,1,0,0,310,41,1,0,0,0,311,312,5,27,0,0,312,43,1,0,0,0,313,314,
        5,35,0,0,314,45,1,0,0,0,315,317,5,37,0,0,316,315,1,0,0,0,317,320,
        1,0,0,0,318,316,1,0,0,0,318,319,1,0,0,0,319,322,1,0,0,0,320,318,
        1,0,0,0,321,323,5,36,0,0,322,321,1,0,0,0,323,324,1,0,0,0,324,322,
        1,0,0,0,324,325,1,0,0,0,325,47,1,0,0,0,326,328,5,37,0,0,327,326,
        1,0,0,0,328,331,1,0,0,0,329,327,1,0,0,0,329,330,1,0,0,0,330,333,
        1,0,0,0,331,329,1,0,0,0,332,334,5,36,0,0,333,332,1,0,0,0,334,335,
        1,0,0,0,335,333,1,0,0,0,335,336,1,0,0,0,336,337,1,0,0,0,337,339,
        5,28,0,0,338,340,5,36,0,0,339,338,1,0,0,0,340,341,1,0,0,0,341,339,
        1,0,0,0,341,342,1,0,0,0,342,49,1,0,0,0,343,344,5,38,0,0,344,51,1,
        0,0,0,345,346,5,7,0,0,346,53,1,0,0,0,347,348,5,8,0,0,348,55,1,0,
        0,0,349,350,5,9,0,0,350,57,1,0,0,0,33,60,62,69,84,91,103,108,120,
        137,139,146,154,165,167,194,200,209,212,222,235,244,256,265,275,
        285,291,301,305,318,324,329,335,341
    ]

class Act_31Parser ( Parser ):

    grammarFileName = "Act_31.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'()'", "'('", "','", "')'", 
                     "'+'", "'-'", "'*'", "'/'", "'^'", "'sqrt('", "'&&'", 
                     "'||'", "'!'", "'<'", "'>'", "'=='", "'>='", "'<='", 
                     "'if'", "'{'", "'}'", "'else'", "'while'", "'return'", 
                     "'main'", "'.'", "'int'", "'float'", "'string'", "'void'", 
                     "'TRUE'", "'FALSE'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INT", "FLOAT", "STRING", "VOID", "TRUE", 
                      "FALSE", "ID", "NUM", "DEC", "STR", "WS" ]

    RULE_prog = 0
    RULE_line = 1
    RULE_type = 2
    RULE_declaration = 3
    RULE_definition = 4
    RULE_value = 5
    RULE_func_call = 6
    RULE_op = 7
    RULE_variable = 8
    RULE_boolean = 9
    RULE_compare = 10
    RULE_if_struct = 11
    RULE_if = 12
    RULE_else_if = 13
    RULE_else = 14
    RULE_while_struct = 15
    RULE_func_struct = 16
    RULE_func_type = 17
    RULE_func = 18
    RULE_func_body = 19
    RULE_return = 20
    RULE_tk_main = 21
    RULE_tk_ID = 22
    RULE_tk_int = 23
    RULE_tk_float = 24
    RULE_tk_string = 25
    RULE_tk_add = 26
    RULE_tk_sub = 27
    RULE_tk_mult = 28

    ruleNames =  [ "prog", "line", "type", "declaration", "definition", 
                   "value", "func_call", "op", "variable", "boolean", "compare", 
                   "if_struct", "if", "else_if", "else", "while_struct", 
                   "func_struct", "func_type", "func", "func_body", "return", 
                   "tk_main", "tk_ID", "tk_int", "tk_float", "tk_string", 
                   "tk_add", "tk_sub", "tk_mult" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    INT=29
    FLOAT=30
    STRING=31
    VOID=32
    TRUE=33
    FALSE=34
    ID=35
    NUM=36
    DEC=37
    STR=38
    WS=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Act_31Parser.LineContext)
            else:
                return self.getTypedRuleContext(Act_31Parser.LineContext,i)


        def func_struct(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Act_31Parser.Func_structContext)
            else:
                return self.getTypedRuleContext(Act_31Parser.Func_structContext,i)


        def getRuleIndex(self):
            return Act_31Parser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = Act_31Parser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 42412802048) != 0):
                self.state = 60
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 58
                    self.line()
                    pass

                elif la_ == 2:
                    self.state = 59
                    self.func_struct()
                    pass


                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(Act_31Parser.DeclarationContext,0)


        def definition(self):
            return self.getTypedRuleContext(Act_31Parser.DefinitionContext,0)


        def getRuleIndex(self):
            return Act_31Parser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = Act_31Parser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.definition()
                self.state = 67
                self.match(Act_31Parser.T__0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(Act_31Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(Act_31Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(Act_31Parser.STRING, 0)

        def getRuleIndex(self):
            return Act_31Parser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = Act_31Parser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(Act_31Parser.TypeContext,0)


        def tk_ID(self):
            return self.getTypedRuleContext(Act_31Parser.Tk_IDContext,0)


        def getRuleIndex(self):
            return Act_31Parser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = Act_31Parser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.type_()
            self.state = 74
            self.tk_ID()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(Act_31Parser.DeclarationContext,0)


        def value(self):
            return self.getTypedRuleContext(Act_31Parser.ValueContext,0)


        def tk_ID(self):
            return self.getTypedRuleContext(Act_31Parser.Tk_IDContext,0)


        def getRuleIndex(self):
            return Act_31Parser.RULE_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinition" ):
                listener.enterDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinition" ):
                listener.exitDefinition(self)




    def definition(self):

        localctx = Act_31Parser.DefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_definition)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29, 30, 31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.declaration()
                self.state = 77
                self.match(Act_31Parser.T__1)
                self.state = 78
                self.value()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.tk_ID()
                self.state = 81
                self.match(Act_31Parser.T__1)
                self.state = 82
                self.value()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tk_int(self):
            return self.getTypedRuleContext(Act_31Parser.Tk_intContext,0)


        def tk_float(self):
            return self.getTypedRuleContext(Act_31Parser.Tk_floatContext,0)


        def tk_string(self):
            return self.getTypedRuleContext(Act_31Parser.Tk_stringContext,0)


        def op(self):
            return self.getTypedRuleContext(Act_31Parser.OpContext,0)


        def func_call(self):
            return self.getTypedRuleContext(Act_31Parser.Func_callContext,0)


        def getRuleIndex(self):
            return Act_31Parser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = Act_31Parser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_value)
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.tk_int()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.tk_float()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.tk_string()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 89
                self.op(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 90
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tk_ID(self):
            return self.getTypedRuleContext(Act_31Parser.Tk_IDContext,0)


        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Act_31Parser.ValueContext)
            else:
                return self.getTypedRuleContext(Act_31Parser.ValueContext,i)


        def getRuleIndex(self):
            return Act_31Parser.RULE_func_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_call" ):
                listener.enterFunc_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_call" ):
                listener.exitFunc_call(self)




    def func_call(self):

        localctx = Act_31Parser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.tk_ID()
                self.state = 94
                self.match(Act_31Parser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.tk_ID()
                self.state = 97
                self.match(Act_31Parser.T__3)
                self.state = 98
                self.value()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 99
                    self.match(Act_31Parser.T__4)
                    self.state = 100
                    self.value()
                    self.state = 105
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 106
                self.match(Act_31Parser.T__5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Act_31Parser.RULE_op

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParContext(OpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Act_31Parser.OpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def op(self):
            return self.getTypedRuleContext(Act_31Parser.OpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPar" ):
                listener.enterPar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPar" ):
                listener.exitPar(self)


    class DivContext(OpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Act_31Parser.OpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Act_31Parser.OpContext)
            else:
                return self.getTypedRuleContext(Act_31Parser.OpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiv" ):
                listener.enterDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiv" ):
                listener.exitDiv(self)


    class SubContext(OpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Act_31Parser.OpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Act_31Parser.OpContext)
            else:
                return self.getTypedRuleContext(Act_31Parser.OpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub" ):
                listener.enterSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub" ):
                listener.exitSub(self)


    class MultContext(OpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Act_31Parser.OpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Act_31Parser.OpContext)
            else:
                return self.getTypedRuleContext(Act_31Parser.OpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMult" ):
                listener.enterMult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMult" ):
                listener.exitMult(self)


    class VarOpContext(OpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Act_31Parser.OpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable(self):
            return self.getTypedRuleContext(Act_31Parser.VariableContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarOp" ):
                listener.enterVarOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarOp" ):
                listener.exitVarOp(self)


    class SqrtContext(OpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Act_31Parser.OpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def op(self):
            return self.getTypedRuleContext(Act_31Parser.OpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSqrt" ):
                listener.enterSqrt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSqrt" ):
                listener.exitSqrt(self)


    class PowContext(OpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Act_31Parser.OpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Act_31Parser.OpContext)
            else:
                return self.getTypedRuleContext(Act_31Parser.OpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPow" ):
                listener.enterPow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPow" ):
                listener.exitPow(self)


    class SumContext(OpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Act_31Parser.OpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Act_31Parser.OpContext)
            else:
                return self.getTypedRuleContext(Act_31Parser.OpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSum" ):
                listener.enterSum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSum" ):
                listener.exitSum(self)



    def op(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Act_31Parser.OpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_op, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                localctx = Act_31Parser.SqrtContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 111
                self.match(Act_31Parser.T__11)
                self.state = 112
                self.op(0)
                self.state = 113
                self.match(Act_31Parser.T__5)
                pass
            elif token in [35, 36, 37, 38]:
                localctx = Act_31Parser.VarOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 115
                self.variable()
                pass
            elif token in [4]:
                localctx = Act_31Parser.ParContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 116
                self.match(Act_31Parser.T__3)
                self.state = 117
                self.op(0)
                self.state = 118
                self.match(Act_31Parser.T__5)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 139
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 137
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = Act_31Parser.SumContext(self, Act_31Parser.OpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_op)
                        self.state = 122
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 123
                        self.match(Act_31Parser.T__6)
                        self.state = 124
                        self.op(9)
                        pass

                    elif la_ == 2:
                        localctx = Act_31Parser.SubContext(self, Act_31Parser.OpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_op)
                        self.state = 125
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 126
                        self.match(Act_31Parser.T__7)
                        self.state = 127
                        self.op(8)
                        pass

                    elif la_ == 3:
                        localctx = Act_31Parser.MultContext(self, Act_31Parser.OpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_op)
                        self.state = 128
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 129
                        self.match(Act_31Parser.T__8)
                        self.state = 130
                        self.op(7)
                        pass

                    elif la_ == 4:
                        localctx = Act_31Parser.DivContext(self, Act_31Parser.OpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_op)
                        self.state = 131
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 132
                        self.match(Act_31Parser.T__9)
                        self.state = 133
                        self.op(6)
                        pass

                    elif la_ == 5:
                        localctx = Act_31Parser.PowContext(self, Act_31Parser.OpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_op)
                        self.state = 134
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 135
                        self.match(Act_31Parser.T__10)
                        self.state = 136
                        self.op(5)
                        pass

             
                self.state = 141
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Act_31Parser.RULE_variable

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringContext(VariableContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Act_31Parser.VariableContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tk_string(self):
            return self.getTypedRuleContext(Act_31Parser.Tk_stringContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)


    class VarContext(VariableContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Act_31Parser.VariableContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tk_ID(self):
            return self.getTypedRuleContext(Act_31Parser.Tk_IDContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)


    class FloatContext(VariableContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Act_31Parser.VariableContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tk_float(self):
            return self.getTypedRuleContext(Act_31Parser.Tk_floatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)


    class IntContext(VariableContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Act_31Parser.VariableContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tk_int(self):
            return self.getTypedRuleContext(Act_31Parser.Tk_intContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def variable(self):

        localctx = Act_31Parser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_variable)
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = Act_31Parser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.tk_int()
                pass

            elif la_ == 2:
                localctx = Act_31Parser.FloatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.tk_float()
                pass

            elif la_ == 3:
                localctx = Act_31Parser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 144
                self.tk_string()
                pass

            elif la_ == 4:
                localctx = Act_31Parser.VarContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 145
                self.tk_ID()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolean(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Act_31Parser.BooleanContext)
            else:
                return self.getTypedRuleContext(Act_31Parser.BooleanContext,i)


        def TRUE(self):
            return self.getToken(Act_31Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(Act_31Parser.FALSE, 0)

        def compare(self):
            return self.getTypedRuleContext(Act_31Parser.CompareContext,0)


        def getRuleIndex(self):
            return Act_31Parser.RULE_boolean

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)



    def boolean(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Act_31Parser.BooleanContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_boolean, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.state = 149
                self.match(Act_31Parser.T__14)
                self.state = 150
                self.boolean(4)
                pass
            elif token in [33]:
                self.state = 151
                self.match(Act_31Parser.TRUE)
                pass
            elif token in [34]:
                self.state = 152
                self.match(Act_31Parser.FALSE)
                pass
            elif token in [4, 35, 36, 37, 38]:
                self.state = 153
                self.compare()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 167
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 165
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = Act_31Parser.BooleanContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean)
                        self.state = 156
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 157
                        self.match(Act_31Parser.T__12)
                        self.state = 158
                        self.boolean(8)
                        pass

                    elif la_ == 2:
                        localctx = Act_31Parser.BooleanContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean)
                        self.state = 159
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 160
                        self.match(Act_31Parser.T__13)
                        self.state = 161
                        self.boolean(7)
                        pass

                    elif la_ == 3:
                        localctx = Act_31Parser.BooleanContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean)
                        self.state = 162
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 163
                        self.match(Act_31Parser.T__10)
                        self.state = 164
                        self.boolean(6)
                        pass

             
                self.state = 169
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CompareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Act_31Parser.VariableContext)
            else:
                return self.getTypedRuleContext(Act_31Parser.VariableContext,i)


        def compare(self):
            return self.getTypedRuleContext(Act_31Parser.CompareContext,0)


        def getRuleIndex(self):
            return Act_31Parser.RULE_compare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompare" ):
                listener.enterCompare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompare" ):
                listener.exitCompare(self)




    def compare(self):

        localctx = Act_31Parser.CompareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_compare)
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.variable()
                self.state = 171
                self.match(Act_31Parser.T__15)
                self.state = 172
                self.variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.variable()
                self.state = 175
                self.match(Act_31Parser.T__16)
                self.state = 176
                self.variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 178
                self.variable()
                self.state = 179
                self.match(Act_31Parser.T__17)
                self.state = 180
                self.variable()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 182
                self.variable()
                self.state = 183
                self.match(Act_31Parser.T__18)
                self.state = 184
                self.variable()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 186
                self.variable()
                self.state = 187
                self.match(Act_31Parser.T__19)
                self.state = 188
                self.variable()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 190
                self.match(Act_31Parser.T__3)
                self.state = 191
                self.compare()
                self.state = 192
                self.match(Act_31Parser.T__5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_structContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_(self):
            return self.getTypedRuleContext(Act_31Parser.IfContext,0)


        def else_(self):
            return self.getTypedRuleContext(Act_31Parser.ElseContext,0)


        def else_if(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Act_31Parser.Else_ifContext)
            else:
                return self.getTypedRuleContext(Act_31Parser.Else_ifContext,i)


        def getRuleIndex(self):
            return Act_31Parser.RULE_if_struct

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_struct" ):
                listener.enterIf_struct(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_struct" ):
                listener.exitIf_struct(self)




    def if_struct(self):

        localctx = Act_31Parser.If_structContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_if_struct)
        self._la = 0 # Token type
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.if_()
                self.state = 200
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 197
                        self.else_if() 
                    self.state = 202
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

                self.state = 203
                self.else_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.if_()
                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==24:
                    self.state = 206
                    self.else_if()
                    self.state = 211
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolean(self):
            return self.getTypedRuleContext(Act_31Parser.BooleanContext,0)


        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Act_31Parser.LineContext)
            else:
                return self.getTypedRuleContext(Act_31Parser.LineContext,i)


        def getRuleIndex(self):
            return Act_31Parser.RULE_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)




    def if_(self):

        localctx = Act_31Parser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(Act_31Parser.T__20)
            self.state = 215
            self.match(Act_31Parser.T__3)
            self.state = 216
            self.boolean(0)
            self.state = 217
            self.match(Act_31Parser.T__5)
            self.state = 218
            self.match(Act_31Parser.T__21)
            self.state = 220 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 219
                self.line()
                self.state = 222 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 38117834752) != 0)):
                    break

            self.state = 224
            self.match(Act_31Parser.T__22)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolean(self):
            return self.getTypedRuleContext(Act_31Parser.BooleanContext,0)


        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Act_31Parser.LineContext)
            else:
                return self.getTypedRuleContext(Act_31Parser.LineContext,i)


        def getRuleIndex(self):
            return Act_31Parser.RULE_else_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_if" ):
                listener.enterElse_if(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_if" ):
                listener.exitElse_if(self)




    def else_if(self):

        localctx = Act_31Parser.Else_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_else_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(Act_31Parser.T__23)
            self.state = 227
            self.match(Act_31Parser.T__20)
            self.state = 228
            self.match(Act_31Parser.T__3)
            self.state = 229
            self.boolean(0)
            self.state = 230
            self.match(Act_31Parser.T__5)
            self.state = 231
            self.match(Act_31Parser.T__21)
            self.state = 233 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 232
                self.line()
                self.state = 235 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 38117834752) != 0)):
                    break

            self.state = 237
            self.match(Act_31Parser.T__22)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Act_31Parser.LineContext)
            else:
                return self.getTypedRuleContext(Act_31Parser.LineContext,i)


        def getRuleIndex(self):
            return Act_31Parser.RULE_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse" ):
                listener.enterElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse" ):
                listener.exitElse(self)




    def else_(self):

        localctx = Act_31Parser.ElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_else)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(Act_31Parser.T__23)
            self.state = 240
            self.match(Act_31Parser.T__21)
            self.state = 242 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 241
                self.line()
                self.state = 244 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 38117834752) != 0)):
                    break

            self.state = 246
            self.match(Act_31Parser.T__22)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_structContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolean(self):
            return self.getTypedRuleContext(Act_31Parser.BooleanContext,0)


        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Act_31Parser.LineContext)
            else:
                return self.getTypedRuleContext(Act_31Parser.LineContext,i)


        def getRuleIndex(self):
            return Act_31Parser.RULE_while_struct

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_struct" ):
                listener.enterWhile_struct(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_struct" ):
                listener.exitWhile_struct(self)




    def while_struct(self):

        localctx = Act_31Parser.While_structContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_while_struct)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(Act_31Parser.T__24)
            self.state = 249
            self.match(Act_31Parser.T__3)
            self.state = 250
            self.boolean(0)
            self.state = 251
            self.match(Act_31Parser.T__5)
            self.state = 252
            self.match(Act_31Parser.T__21)
            self.state = 254 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 253
                self.line()
                self.state = 256 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 38117834752) != 0)):
                    break

            self.state = 258
            self.match(Act_31Parser.T__22)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_structContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func(self):
            return self.getTypedRuleContext(Act_31Parser.FuncContext,0)


        def func_body(self):
            return self.getTypedRuleContext(Act_31Parser.Func_bodyContext,0)


        def getRuleIndex(self):
            return Act_31Parser.RULE_func_struct

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_struct" ):
                listener.enterFunc_struct(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_struct" ):
                listener.exitFunc_struct(self)




    def func_struct(self):

        localctx = Act_31Parser.Func_structContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_func_struct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.func()
            self.state = 261
            self.func_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(Act_31Parser.TypeContext,0)


        def VOID(self):
            return self.getToken(Act_31Parser.VOID, 0)

        def getRuleIndex(self):
            return Act_31Parser.RULE_func_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_type" ):
                listener.enterFunc_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_type" ):
                listener.exitFunc_type(self)




    def func_type(self):

        localctx = Act_31Parser.Func_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_func_type)
        try:
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29, 30, 31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.type_()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.match(Act_31Parser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_type(self):
            return self.getTypedRuleContext(Act_31Parser.Func_typeContext,0)


        def tk_ID(self):
            return self.getTypedRuleContext(Act_31Parser.Tk_IDContext,0)


        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Act_31Parser.DeclarationContext)
            else:
                return self.getTypedRuleContext(Act_31Parser.DeclarationContext,i)


        def getRuleIndex(self):
            return Act_31Parser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)




    def func(self):

        localctx = Act_31Parser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.func_type()
                self.state = 268
                self.tk_ID()
                self.state = 269
                self.match(Act_31Parser.T__3)
                self.state = 270
                self.declaration()
                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 271
                    self.match(Act_31Parser.T__4)
                    self.state = 272
                    self.declaration()
                    self.state = 277
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 278
                self.match(Act_31Parser.T__5)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.func_type()
                self.state = 281
                self.tk_ID()
                self.state = 282
                self.match(Act_31Parser.T__3)
                self.state = 283
                self.match(Act_31Parser.T__5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_(self):
            return self.getTypedRuleContext(Act_31Parser.ReturnContext,0)


        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Act_31Parser.LineContext)
            else:
                return self.getTypedRuleContext(Act_31Parser.LineContext,i)


        def getRuleIndex(self):
            return Act_31Parser.RULE_func_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_body" ):
                listener.enterFunc_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_body" ):
                listener.exitFunc_body(self)




    def func_body(self):

        localctx = Act_31Parser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_func_body)
        self._la = 0 # Token type
        try:
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.match(Act_31Parser.T__21)
                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 38117834752) != 0):
                    self.state = 288
                    self.line()
                    self.state = 293
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 294
                self.return_()
                self.state = 295
                self.match(Act_31Parser.T__22)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.match(Act_31Parser.T__21)
                self.state = 301
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 38117834752) != 0):
                    self.state = 298
                    self.line()
                    self.state = 303
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 304
                self.match(Act_31Parser.T__22)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(Act_31Parser.VariableContext,0)


        def getRuleIndex(self):
            return Act_31Parser.RULE_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)




    def return_(self):

        localctx = Act_31Parser.ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(Act_31Parser.T__25)
            self.state = 308
            self.variable()
            self.state = 309
            self.match(Act_31Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tk_mainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Act_31Parser.RULE_tk_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTk_main" ):
                listener.enterTk_main(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTk_main" ):
                listener.exitTk_main(self)




    def tk_main(self):

        localctx = Act_31Parser.Tk_mainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_tk_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(Act_31Parser.T__26)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tk_IDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Act_31Parser.ID, 0)

        def getRuleIndex(self):
            return Act_31Parser.RULE_tk_ID

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTk_ID" ):
                listener.enterTk_ID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTk_ID" ):
                listener.exitTk_ID(self)




    def tk_ID(self):

        localctx = Act_31Parser.Tk_IDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_tk_ID)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(Act_31Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tk_intContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEC(self, i:int=None):
            if i is None:
                return self.getTokens(Act_31Parser.DEC)
            else:
                return self.getToken(Act_31Parser.DEC, i)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(Act_31Parser.NUM)
            else:
                return self.getToken(Act_31Parser.NUM, i)

        def getRuleIndex(self):
            return Act_31Parser.RULE_tk_int

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTk_int" ):
                listener.enterTk_int(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTk_int" ):
                listener.exitTk_int(self)




    def tk_int(self):

        localctx = Act_31Parser.Tk_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_tk_int)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 315
                self.match(Act_31Parser.DEC)
                self.state = 320
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 322 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 321
                    self.match(Act_31Parser.NUM)

                else:
                    raise NoViableAltException(self)
                self.state = 324 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tk_floatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEC(self, i:int=None):
            if i is None:
                return self.getTokens(Act_31Parser.DEC)
            else:
                return self.getToken(Act_31Parser.DEC, i)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(Act_31Parser.NUM)
            else:
                return self.getToken(Act_31Parser.NUM, i)

        def getRuleIndex(self):
            return Act_31Parser.RULE_tk_float

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTk_float" ):
                listener.enterTk_float(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTk_float" ):
                listener.exitTk_float(self)




    def tk_float(self):

        localctx = Act_31Parser.Tk_floatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_tk_float)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 326
                self.match(Act_31Parser.DEC)
                self.state = 331
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 333 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 332
                self.match(Act_31Parser.NUM)
                self.state = 335 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==36):
                    break

            self.state = 337
            self.match(Act_31Parser.T__27)
            self.state = 339 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 338
                    self.match(Act_31Parser.NUM)

                else:
                    raise NoViableAltException(self)
                self.state = 341 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tk_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR(self):
            return self.getToken(Act_31Parser.STR, 0)

        def getRuleIndex(self):
            return Act_31Parser.RULE_tk_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTk_string" ):
                listener.enterTk_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTk_string" ):
                listener.exitTk_string(self)




    def tk_string(self):

        localctx = Act_31Parser.Tk_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_tk_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(Act_31Parser.STR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tk_addContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Act_31Parser.RULE_tk_add

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTk_add" ):
                listener.enterTk_add(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTk_add" ):
                listener.exitTk_add(self)




    def tk_add(self):

        localctx = Act_31Parser.Tk_addContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_tk_add)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(Act_31Parser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tk_subContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Act_31Parser.RULE_tk_sub

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTk_sub" ):
                listener.enterTk_sub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTk_sub" ):
                listener.exitTk_sub(self)




    def tk_sub(self):

        localctx = Act_31Parser.Tk_subContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_tk_sub)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(Act_31Parser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tk_multContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Act_31Parser.RULE_tk_mult

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTk_mult" ):
                listener.enterTk_mult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTk_mult" ):
                listener.exitTk_mult(self)




    def tk_mult(self):

        localctx = Act_31Parser.Tk_multContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_tk_mult)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(Act_31Parser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.op_sempred
        self._predicates[9] = self.boolean_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def op_sempred(self, localctx:OpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

    def boolean_sempred(self, localctx:BooleanContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 5)
         




