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
        4,1,38,333,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,1,0,5,0,59,8,0,10,0,12,0,62,9,0,1,1,1,1,1,1,1,1,3,
        1,68,8,1,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,
        83,8,4,1,5,1,5,1,5,1,5,1,5,3,5,90,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,3,6,102,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,5,6,119,8,6,10,6,12,6,122,9,6,1,7,1,7,1,7,
        1,7,3,7,128,8,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,136,8,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,5,8,147,8,8,10,8,12,8,150,9,8,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,3,9,176,8,9,1,10,1,10,5,10,180,8,10,10,10,
        12,10,183,9,10,1,10,1,10,1,10,1,10,5,10,189,8,10,10,10,12,10,192,
        9,10,3,10,194,8,10,1,11,1,11,1,11,1,11,1,11,1,11,4,11,202,8,11,11,
        11,12,11,203,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,4,12,215,
        8,12,11,12,12,12,216,1,12,1,12,1,13,1,13,1,13,4,13,224,8,13,11,13,
        12,13,225,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,4,14,236,8,14,
        11,14,12,14,237,1,14,1,14,1,15,1,15,1,15,1,16,1,16,3,16,247,8,16,
        1,17,1,17,1,17,1,17,1,17,1,17,5,17,255,8,17,10,17,12,17,258,9,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,267,8,17,1,18,1,18,5,18,
        271,8,18,10,18,12,18,274,9,18,1,18,1,18,1,18,1,18,1,18,5,18,281,
        8,18,10,18,12,18,284,9,18,1,18,3,18,287,8,18,1,19,1,19,1,19,1,19,
        1,20,1,20,1,21,1,21,1,22,5,22,298,8,22,10,22,12,22,301,9,22,1,22,
        4,22,304,8,22,11,22,12,22,305,1,23,5,23,309,8,23,10,23,12,23,312,
        9,23,1,23,4,23,315,8,23,11,23,12,23,316,1,23,1,23,4,23,321,8,23,
        11,23,12,23,322,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,27,0,2,
        12,16,28,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,0,1,1,0,28,30,351,0,60,1,0,0,0,2,67,1,0,
        0,0,4,69,1,0,0,0,6,71,1,0,0,0,8,82,1,0,0,0,10,89,1,0,0,0,12,101,
        1,0,0,0,14,127,1,0,0,0,16,135,1,0,0,0,18,175,1,0,0,0,20,193,1,0,
        0,0,22,195,1,0,0,0,24,207,1,0,0,0,26,220,1,0,0,0,28,229,1,0,0,0,
        30,241,1,0,0,0,32,246,1,0,0,0,34,266,1,0,0,0,36,286,1,0,0,0,38,288,
        1,0,0,0,40,292,1,0,0,0,42,294,1,0,0,0,44,299,1,0,0,0,46,310,1,0,
        0,0,48,324,1,0,0,0,50,326,1,0,0,0,52,328,1,0,0,0,54,330,1,0,0,0,
        56,59,3,2,1,0,57,59,3,30,15,0,58,56,1,0,0,0,58,57,1,0,0,0,59,62,
        1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,1,1,0,0,0,62,60,1,0,0,0,63,
        68,3,6,3,0,64,65,3,8,4,0,65,66,5,1,0,0,66,68,1,0,0,0,67,63,1,0,0,
        0,67,64,1,0,0,0,68,3,1,0,0,0,69,70,7,0,0,0,70,5,1,0,0,0,71,72,3,
        4,2,0,72,73,3,42,21,0,73,7,1,0,0,0,74,75,3,6,3,0,75,76,5,2,0,0,76,
        77,3,10,5,0,77,83,1,0,0,0,78,79,3,42,21,0,79,80,5,2,0,0,80,81,3,
        10,5,0,81,83,1,0,0,0,82,74,1,0,0,0,82,78,1,0,0,0,83,9,1,0,0,0,84,
        90,3,44,22,0,85,90,3,46,23,0,86,90,3,48,24,0,87,90,3,48,24,0,88,
        90,3,12,6,0,89,84,1,0,0,0,89,85,1,0,0,0,89,86,1,0,0,0,89,87,1,0,
        0,0,89,88,1,0,0,0,90,11,1,0,0,0,91,92,6,6,-1,0,92,93,5,8,0,0,93,
        94,3,12,6,0,94,95,5,9,0,0,95,102,1,0,0,0,96,102,3,14,7,0,97,98,5,
        10,0,0,98,99,3,12,6,0,99,100,5,9,0,0,100,102,1,0,0,0,101,91,1,0,
        0,0,101,96,1,0,0,0,101,97,1,0,0,0,102,120,1,0,0,0,103,104,10,8,0,
        0,104,105,5,3,0,0,105,119,3,12,6,9,106,107,10,7,0,0,107,108,5,4,
        0,0,108,119,3,12,6,8,109,110,10,6,0,0,110,111,5,5,0,0,111,119,3,
        12,6,7,112,113,10,5,0,0,113,114,5,6,0,0,114,119,3,12,6,6,115,116,
        10,4,0,0,116,117,5,7,0,0,117,119,3,12,6,5,118,103,1,0,0,0,118,106,
        1,0,0,0,118,109,1,0,0,0,118,112,1,0,0,0,118,115,1,0,0,0,119,122,
        1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,13,1,0,0,0,122,120,1,
        0,0,0,123,128,3,42,21,0,124,128,3,44,22,0,125,128,3,46,23,0,126,
        128,3,48,24,0,127,123,1,0,0,0,127,124,1,0,0,0,127,125,1,0,0,0,127,
        126,1,0,0,0,128,15,1,0,0,0,129,130,6,8,-1,0,130,131,5,13,0,0,131,
        136,3,16,8,4,132,136,5,32,0,0,133,136,5,33,0,0,134,136,3,18,9,0,
        135,129,1,0,0,0,135,132,1,0,0,0,135,133,1,0,0,0,135,134,1,0,0,0,
        136,148,1,0,0,0,137,138,10,7,0,0,138,139,5,11,0,0,139,147,3,16,8,
        8,140,141,10,6,0,0,141,142,5,12,0,0,142,147,3,16,8,7,143,144,10,
        5,0,0,144,145,5,7,0,0,145,147,3,16,8,6,146,137,1,0,0,0,146,140,1,
        0,0,0,146,143,1,0,0,0,147,150,1,0,0,0,148,146,1,0,0,0,148,149,1,
        0,0,0,149,17,1,0,0,0,150,148,1,0,0,0,151,152,3,14,7,0,152,153,5,
        14,0,0,153,154,3,14,7,0,154,176,1,0,0,0,155,156,3,14,7,0,156,157,
        5,15,0,0,157,158,3,14,7,0,158,176,1,0,0,0,159,160,3,14,7,0,160,161,
        5,16,0,0,161,162,3,14,7,0,162,176,1,0,0,0,163,164,3,14,7,0,164,165,
        5,17,0,0,165,166,3,14,7,0,166,176,1,0,0,0,167,168,3,14,7,0,168,169,
        5,18,0,0,169,170,3,14,7,0,170,176,1,0,0,0,171,172,5,10,0,0,172,173,
        3,18,9,0,173,174,5,9,0,0,174,176,1,0,0,0,175,151,1,0,0,0,175,155,
        1,0,0,0,175,159,1,0,0,0,175,163,1,0,0,0,175,167,1,0,0,0,175,171,
        1,0,0,0,176,19,1,0,0,0,177,181,3,22,11,0,178,180,3,24,12,0,179,178,
        1,0,0,0,180,183,1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,184,
        1,0,0,0,183,181,1,0,0,0,184,185,3,26,13,0,185,194,1,0,0,0,186,190,
        3,22,11,0,187,189,3,24,12,0,188,187,1,0,0,0,189,192,1,0,0,0,190,
        188,1,0,0,0,190,191,1,0,0,0,191,194,1,0,0,0,192,190,1,0,0,0,193,
        177,1,0,0,0,193,186,1,0,0,0,194,21,1,0,0,0,195,196,5,19,0,0,196,
        197,5,10,0,0,197,198,3,16,8,0,198,199,5,9,0,0,199,201,5,20,0,0,200,
        202,3,2,1,0,201,200,1,0,0,0,202,203,1,0,0,0,203,201,1,0,0,0,203,
        204,1,0,0,0,204,205,1,0,0,0,205,206,5,21,0,0,206,23,1,0,0,0,207,
        208,5,22,0,0,208,209,5,19,0,0,209,210,5,10,0,0,210,211,3,16,8,0,
        211,212,5,9,0,0,212,214,5,20,0,0,213,215,3,2,1,0,214,213,1,0,0,0,
        215,216,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,218,1,0,0,0,
        218,219,5,21,0,0,219,25,1,0,0,0,220,221,5,22,0,0,221,223,5,20,0,
        0,222,224,3,2,1,0,223,222,1,0,0,0,224,225,1,0,0,0,225,223,1,0,0,
        0,225,226,1,0,0,0,226,227,1,0,0,0,227,228,5,21,0,0,228,27,1,0,0,
        0,229,230,5,23,0,0,230,231,5,10,0,0,231,232,3,16,8,0,232,233,5,9,
        0,0,233,235,5,20,0,0,234,236,3,2,1,0,235,234,1,0,0,0,236,237,1,0,
        0,0,237,235,1,0,0,0,237,238,1,0,0,0,238,239,1,0,0,0,239,240,5,21,
        0,0,240,29,1,0,0,0,241,242,3,34,17,0,242,243,3,36,18,0,243,31,1,
        0,0,0,244,247,3,4,2,0,245,247,5,31,0,0,246,244,1,0,0,0,246,245,1,
        0,0,0,247,33,1,0,0,0,248,249,3,32,16,0,249,250,3,42,21,0,250,251,
        5,10,0,0,251,256,3,6,3,0,252,253,5,24,0,0,253,255,3,6,3,0,254,252,
        1,0,0,0,255,258,1,0,0,0,256,254,1,0,0,0,256,257,1,0,0,0,257,259,
        1,0,0,0,258,256,1,0,0,0,259,260,5,9,0,0,260,267,1,0,0,0,261,262,
        3,32,16,0,262,263,3,42,21,0,263,264,5,10,0,0,264,265,5,9,0,0,265,
        267,1,0,0,0,266,248,1,0,0,0,266,261,1,0,0,0,267,35,1,0,0,0,268,272,
        5,20,0,0,269,271,3,2,1,0,270,269,1,0,0,0,271,274,1,0,0,0,272,270,
        1,0,0,0,272,273,1,0,0,0,273,275,1,0,0,0,274,272,1,0,0,0,275,276,
        3,38,19,0,276,277,5,21,0,0,277,287,1,0,0,0,278,282,5,20,0,0,279,
        281,3,2,1,0,280,279,1,0,0,0,281,284,1,0,0,0,282,280,1,0,0,0,282,
        283,1,0,0,0,283,285,1,0,0,0,284,282,1,0,0,0,285,287,5,21,0,0,286,
        268,1,0,0,0,286,278,1,0,0,0,287,37,1,0,0,0,288,289,5,25,0,0,289,
        290,3,14,7,0,290,291,5,1,0,0,291,39,1,0,0,0,292,293,5,26,0,0,293,
        41,1,0,0,0,294,295,5,34,0,0,295,43,1,0,0,0,296,298,5,36,0,0,297,
        296,1,0,0,0,298,301,1,0,0,0,299,297,1,0,0,0,299,300,1,0,0,0,300,
        303,1,0,0,0,301,299,1,0,0,0,302,304,5,35,0,0,303,302,1,0,0,0,304,
        305,1,0,0,0,305,303,1,0,0,0,305,306,1,0,0,0,306,45,1,0,0,0,307,309,
        5,36,0,0,308,307,1,0,0,0,309,312,1,0,0,0,310,308,1,0,0,0,310,311,
        1,0,0,0,311,314,1,0,0,0,312,310,1,0,0,0,313,315,5,35,0,0,314,313,
        1,0,0,0,315,316,1,0,0,0,316,314,1,0,0,0,316,317,1,0,0,0,317,318,
        1,0,0,0,318,320,5,27,0,0,319,321,5,35,0,0,320,319,1,0,0,0,321,322,
        1,0,0,0,322,320,1,0,0,0,322,323,1,0,0,0,323,47,1,0,0,0,324,325,5,
        37,0,0,325,49,1,0,0,0,326,327,5,3,0,0,327,51,1,0,0,0,328,329,5,4,
        0,0,329,53,1,0,0,0,330,331,5,5,0,0,331,55,1,0,0,0,31,58,60,67,82,
        89,101,118,120,127,135,146,148,175,181,190,193,203,216,225,237,246,
        256,266,272,282,286,299,305,310,316,322
    ]

class Act_31Parser ( Parser ):

    grammarFileName = "Act_31.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'+'", "'-'", "'*'", "'/'", 
                     "'^'", "'sqrt('", "')'", "'('", "'&&'", "'||'", "'!'", 
                     "'<'", "'>'", "'=='", "'>='", "'<='", "'if'", "'{'", 
                     "'}'", "'else'", "'while'", "','", "'return'", "'main'", 
                     "'.'", "'int'", "'float'", "'string'", "'void'", "'TRUE'", 
                     "'FALSE'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT", "FLOAT", "STRING", "VOID", "TRUE", "FALSE", 
                      "ID", "NUM", "DEC", "STR", "WS" ]

    RULE_prog = 0
    RULE_line = 1
    RULE_type = 2
    RULE_declaration = 3
    RULE_definition = 4
    RULE_value = 5
    RULE_op = 6
    RULE_variable = 7
    RULE_boolean = 8
    RULE_compare = 9
    RULE_if_struct = 10
    RULE_if = 11
    RULE_else_if = 12
    RULE_else = 13
    RULE_while_struct = 14
    RULE_func_struct = 15
    RULE_func_type = 16
    RULE_func = 17
    RULE_func_body = 18
    RULE_return = 19
    RULE_tk_main = 20
    RULE_tk_ID = 21
    RULE_tk_int = 22
    RULE_tk_float = 23
    RULE_tk_string = 24
    RULE_tk_add = 25
    RULE_tk_sub = 26
    RULE_tk_mult = 27

    ruleNames =  [ "prog", "line", "type", "declaration", "definition", 
                   "value", "op", "variable", "boolean", "compare", "if_struct", 
                   "if", "else_if", "else", "while_struct", "func_struct", 
                   "func_type", "func", "func_body", "return", "tk_main", 
                   "tk_ID", "tk_int", "tk_float", "tk_string", "tk_add", 
                   "tk_sub", "tk_mult" ]

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
    INT=28
    FLOAT=29
    STRING=30
    VOID=31
    TRUE=32
    FALSE=33
    ID=34
    NUM=35
    DEC=36
    STR=37
    WS=38

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
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 21206401024) != 0):
                self.state = 58
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 56
                    self.line()
                    pass

                elif la_ == 2:
                    self.state = 57
                    self.func_struct()
                    pass


                self.state = 62
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
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.definition()
                self.state = 65
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
            self.state = 69
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1879048192) != 0)):
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
            self.state = 71
            self.type_()
            self.state = 72
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
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28, 29, 30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.declaration()
                self.state = 75
                self.match(Act_31Parser.T__1)
                self.state = 76
                self.value()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.tk_ID()
                self.state = 79
                self.match(Act_31Parser.T__1)
                self.state = 80
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
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.tk_int()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.tk_float()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.tk_string()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 87
                self.tk_string()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 88
                self.op(0)
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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_op, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                localctx = Act_31Parser.SqrtContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 92
                self.match(Act_31Parser.T__7)
                self.state = 93
                self.op(0)
                self.state = 94
                self.match(Act_31Parser.T__8)
                pass
            elif token in [34, 35, 36, 37]:
                localctx = Act_31Parser.VarOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 96
                self.variable()
                pass
            elif token in [10]:
                localctx = Act_31Parser.ParContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 97
                self.match(Act_31Parser.T__9)
                self.state = 98
                self.op(0)
                self.state = 99
                self.match(Act_31Parser.T__8)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 120
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 118
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = Act_31Parser.SumContext(self, Act_31Parser.OpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_op)
                        self.state = 103
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 104
                        self.match(Act_31Parser.T__2)
                        self.state = 105
                        self.op(9)
                        pass

                    elif la_ == 2:
                        localctx = Act_31Parser.SubContext(self, Act_31Parser.OpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_op)
                        self.state = 106
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 107
                        self.match(Act_31Parser.T__3)
                        self.state = 108
                        self.op(8)
                        pass

                    elif la_ == 3:
                        localctx = Act_31Parser.MultContext(self, Act_31Parser.OpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_op)
                        self.state = 109
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 110
                        self.match(Act_31Parser.T__4)
                        self.state = 111
                        self.op(7)
                        pass

                    elif la_ == 4:
                        localctx = Act_31Parser.DivContext(self, Act_31Parser.OpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_op)
                        self.state = 112
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 113
                        self.match(Act_31Parser.T__5)
                        self.state = 114
                        self.op(6)
                        pass

                    elif la_ == 5:
                        localctx = Act_31Parser.PowContext(self, Act_31Parser.OpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_op)
                        self.state = 115
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 116
                        self.match(Act_31Parser.T__6)
                        self.state = 117
                        self.op(5)
                        pass

             
                self.state = 122
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        self.enterRule(localctx, 14, self.RULE_variable)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = Act_31Parser.VarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.tk_ID()
                pass

            elif la_ == 2:
                localctx = Act_31Parser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.tk_int()
                pass

            elif la_ == 3:
                localctx = Act_31Parser.FloatContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.tk_float()
                pass

            elif la_ == 4:
                localctx = Act_31Parser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 126
                self.tk_string()
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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_boolean, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 130
                self.match(Act_31Parser.T__12)
                self.state = 131
                self.boolean(4)
                pass
            elif token in [32]:
                self.state = 132
                self.match(Act_31Parser.TRUE)
                pass
            elif token in [33]:
                self.state = 133
                self.match(Act_31Parser.FALSE)
                pass
            elif token in [10, 34, 35, 36, 37]:
                self.state = 134
                self.compare()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 148
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 146
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = Act_31Parser.BooleanContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean)
                        self.state = 137
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 138
                        self.match(Act_31Parser.T__10)
                        self.state = 139
                        self.boolean(8)
                        pass

                    elif la_ == 2:
                        localctx = Act_31Parser.BooleanContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean)
                        self.state = 140
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 141
                        self.match(Act_31Parser.T__11)
                        self.state = 142
                        self.boolean(7)
                        pass

                    elif la_ == 3:
                        localctx = Act_31Parser.BooleanContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean)
                        self.state = 143
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 144
                        self.match(Act_31Parser.T__6)
                        self.state = 145
                        self.boolean(6)
                        pass

             
                self.state = 150
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        self.enterRule(localctx, 18, self.RULE_compare)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.variable()
                self.state = 152
                self.match(Act_31Parser.T__13)
                self.state = 153
                self.variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.variable()
                self.state = 156
                self.match(Act_31Parser.T__14)
                self.state = 157
                self.variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 159
                self.variable()
                self.state = 160
                self.match(Act_31Parser.T__15)
                self.state = 161
                self.variable()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 163
                self.variable()
                self.state = 164
                self.match(Act_31Parser.T__16)
                self.state = 165
                self.variable()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 167
                self.variable()
                self.state = 168
                self.match(Act_31Parser.T__17)
                self.state = 169
                self.variable()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 171
                self.match(Act_31Parser.T__9)
                self.state = 172
                self.compare()
                self.state = 173
                self.match(Act_31Parser.T__8)
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
        self.enterRule(localctx, 20, self.RULE_if_struct)
        self._la = 0 # Token type
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.if_()
                self.state = 181
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 178
                        self.else_if() 
                    self.state = 183
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                self.state = 184
                self.else_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.if_()
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==22:
                    self.state = 187
                    self.else_if()
                    self.state = 192
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
        self.enterRule(localctx, 22, self.RULE_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(Act_31Parser.T__18)
            self.state = 196
            self.match(Act_31Parser.T__9)
            self.state = 197
            self.boolean(0)
            self.state = 198
            self.match(Act_31Parser.T__8)
            self.state = 199
            self.match(Act_31Parser.T__19)
            self.state = 201 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 200
                self.line()
                self.state = 203 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 19058917376) != 0)):
                    break

            self.state = 205
            self.match(Act_31Parser.T__20)
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
        self.enterRule(localctx, 24, self.RULE_else_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(Act_31Parser.T__21)
            self.state = 208
            self.match(Act_31Parser.T__18)
            self.state = 209
            self.match(Act_31Parser.T__9)
            self.state = 210
            self.boolean(0)
            self.state = 211
            self.match(Act_31Parser.T__8)
            self.state = 212
            self.match(Act_31Parser.T__19)
            self.state = 214 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 213
                self.line()
                self.state = 216 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 19058917376) != 0)):
                    break

            self.state = 218
            self.match(Act_31Parser.T__20)
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
        self.enterRule(localctx, 26, self.RULE_else)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(Act_31Parser.T__21)
            self.state = 221
            self.match(Act_31Parser.T__19)
            self.state = 223 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 222
                self.line()
                self.state = 225 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 19058917376) != 0)):
                    break

            self.state = 227
            self.match(Act_31Parser.T__20)
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
        self.enterRule(localctx, 28, self.RULE_while_struct)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(Act_31Parser.T__22)
            self.state = 230
            self.match(Act_31Parser.T__9)
            self.state = 231
            self.boolean(0)
            self.state = 232
            self.match(Act_31Parser.T__8)
            self.state = 233
            self.match(Act_31Parser.T__19)
            self.state = 235 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 234
                self.line()
                self.state = 237 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 19058917376) != 0)):
                    break

            self.state = 239
            self.match(Act_31Parser.T__20)
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
        self.enterRule(localctx, 30, self.RULE_func_struct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.func()
            self.state = 242
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
        self.enterRule(localctx, 32, self.RULE_func_type)
        try:
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28, 29, 30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.type_()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
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
        self.enterRule(localctx, 34, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.func_type()
                self.state = 249
                self.tk_ID()
                self.state = 250
                self.match(Act_31Parser.T__9)
                self.state = 251
                self.declaration()
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==24:
                    self.state = 252
                    self.match(Act_31Parser.T__23)
                    self.state = 253
                    self.declaration()
                    self.state = 258
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 259
                self.match(Act_31Parser.T__8)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.func_type()
                self.state = 262
                self.tk_ID()
                self.state = 263
                self.match(Act_31Parser.T__9)
                self.state = 264
                self.match(Act_31Parser.T__8)
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
        self.enterRule(localctx, 36, self.RULE_func_body)
        self._la = 0 # Token type
        try:
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.match(Act_31Parser.T__19)
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 19058917376) != 0):
                    self.state = 269
                    self.line()
                    self.state = 274
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 275
                self.return_()
                self.state = 276
                self.match(Act_31Parser.T__20)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.match(Act_31Parser.T__19)
                self.state = 282
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 19058917376) != 0):
                    self.state = 279
                    self.line()
                    self.state = 284
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 285
                self.match(Act_31Parser.T__20)
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
        self.enterRule(localctx, 38, self.RULE_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(Act_31Parser.T__24)
            self.state = 289
            self.variable()
            self.state = 290
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
        self.enterRule(localctx, 40, self.RULE_tk_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(Act_31Parser.T__25)
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
        self.enterRule(localctx, 42, self.RULE_tk_ID)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
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
        self.enterRule(localctx, 44, self.RULE_tk_int)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 296
                self.match(Act_31Parser.DEC)
                self.state = 301
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 303 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 302
                    self.match(Act_31Parser.NUM)

                else:
                    raise NoViableAltException(self)
                self.state = 305 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        self.enterRule(localctx, 46, self.RULE_tk_float)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 307
                self.match(Act_31Parser.DEC)
                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 314 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 313
                self.match(Act_31Parser.NUM)
                self.state = 316 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==35):
                    break

            self.state = 318
            self.match(Act_31Parser.T__26)
            self.state = 320 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 319
                    self.match(Act_31Parser.NUM)

                else:
                    raise NoViableAltException(self)
                self.state = 322 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        self.enterRule(localctx, 48, self.RULE_tk_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
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
        self.enterRule(localctx, 50, self.RULE_tk_add)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(Act_31Parser.T__2)
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
        self.enterRule(localctx, 52, self.RULE_tk_sub)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(Act_31Parser.T__3)
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
        self.enterRule(localctx, 54, self.RULE_tk_mult)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(Act_31Parser.T__4)
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
        self._predicates[6] = self.op_sempred
        self._predicates[8] = self.boolean_sempred
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
         




