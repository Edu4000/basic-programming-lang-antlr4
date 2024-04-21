from Grammar.Act_31Listener import Act_31Listener
from Grammar.Act_31Parser import Act_31Parser


class ListenerFunc(Act_31Listener):

    def __init__(self, table):
        self.inner_table = {}
        self.insideFunction = False
        self.funcName = None
        self.returnValue = False

    def enterFunc(self, ctx: Act_31Parser.FuncContext):
        self.insideFunction = True
        self.funcName = ctx.getChild(1).getText()
        self.inner_table[self.funcName] = ctx.getChild(0).getText()

    def enterDeclaration(self, ctx: Act_31Parser.DeclarationContext):
        if not self.insideFunction:
            return

        type = ctx.getChild(0).getText()
        var = ctx.getChild(1).getText()

        if var in self.inner_table.keys():
            raise Exception(
                f"Duplicate declaration at {str(ctx.start).removesuffix(']').split(',')[-1]}"
            )
        else:
            self.inner_table[var] = type

    def exitFunc_struct(self, ctx: Act_31Parser.Func_structContext):
        if not self.returnValue and self.inner_table[self.funcName] != "void":
            raise Exception(
                f"Expected return value '{self.inner_table[self.funcName]}' and got none. Line {str(ctx.start).removesuffix(']').split[','][-1]}"
            )
        if self.returnValue and self.inner_table[self.funcName] == "void":
            raise Exception(
                f"Void function cannot have a return statement. Line {str(ctx.start).removesuffix(']').split[','][-1]}"
            )

        self.returnValue = False
        self.insideFunction = False
        self.funcName = None

    def enterReturn(self, ctx: Act_31Parser.ReturnContext):
        self.returnValue = True

    def enterFunc_call(self, ctx: Act_31Parser.Func_callContext):
        if (
            self.returnValue
            and self.inner_table[self.funcName]
            != self.inner_table["*" + ctx.getChild(0).getText()]
        ):
            raise Exception(
                f"Function is declared to return '{self.inner_table[self.funcName]}' but return value '{self.inner_table[ctx.getChild(0).getText()]}' value was received at {self.getLine(ctx)}."
            )

    def enterTk_ID(self, ctx: Act_31Parser.Tk_IDContext):
        if (
            self.returnValue
            and self.inner_table[self.funcName] != self.inner_table[ctx.getText()]
        ):
            raise Exception(
                f"Function is declared to return '{self.inner_table[self.funcName]}' but '{self.inner_table[ctx.getText()]}' value was received at {self.getLine(ctx)}."
            )

    def enterTk_int(self, ctx: Act_31Parser.Tk_intContext):
        if self.returnValue and self.inner_table[self.funcName] != "int":
            raise Exception(
                f"Function is declared to return '{self.inner_table[self.funcName]}' but 'int' value was received at {self.getLine(ctx)}."
            )

    def enterTk_float(self, ctx: Act_31Parser.Tk_floatContext):
        if self.returnValue and self.inner_table[self.funcName] != "float":
            raise Exception(
                f"Function is declared to return '{self.inner_table[self.funcName]}' but 'float' value was received at {self.getLine(ctx)}."
            )

    def enterTk_string(self, ctx: Act_31Parser.Tk_stringContext):
        if self.returnValue and self.inner_table[self.funcName] != "string":
            raise Exception(
                f"Function is declared to return '{self.inner_table[self.funcName]}' but 'string' value was received at {self.getLine(ctx)}."
            )

    def getLine(self, ctx):
        return str(ctx.start).removesuffix("]").split(",")[-1]
