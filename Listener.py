from Grammar.Act_31Listener import Act_31Listener
from Grammar.Act_31Parser import Act_31Parser
import token


class Listener(Act_31Listener):

    def __init__(self):
        self.table = {}
        self.funcDefinition = False
        self.funcCall = False

    # Creating reference table
    def enterDeclaration(self, ctx: Act_31Parser.DeclarationContext):
        type = ctx.getChild(0).getText()
        var = ctx.getChild(1).getText()

        if self.funcDefinition:
            return

        if var in self.table.keys():
            raise Exception(
                f"Duplicate declaration at {str(ctx.start).removesuffix(']').split(',')[-1]}"
            )
        else:
            self.table[var] = type

    def enterFunc_struct(self, ctx: Act_31Parser.Func_structContext):
        self.funcDefinition = True

    def enterFunc(self, ctx: Act_31Parser.FuncContext):
        type = ctx.getChild(0).getText()
        var = "*" + ctx.getChild(1).getText()

        if var in self.table.keys():
            raise Exception(
                f"Duplicate function declaration at {str(ctx.start).removesuffix(']').split(',')[-1]}"
            )
        else:
            self.table[var] = type

    def exitFunc(self, ctx: Act_31Parser.FuncContext):
        self.funcDefinition = False

    def enterFunc_call(self, ctx: Act_31Parser.Func_callContext):
        self.funcCall = True

        var = "*" + ctx.getChild(0).getText()

        if var not in self.table.keys():
            raise Exception(
                f"Not declared function '{ctx.getChild(0).getText()}' at {str(ctx.start).removesuffix(']').split(',')[-1]}"
            )

    def exitFunc_call(self, ctx: Act_31Parser.Func_callContext):
        self.funcCall = False

    # Makins sure variable reference exists
    def enterTk_ID(self, ctx: Act_31Parser.Tk_IDContext):
        var = ctx.getChild(0).getText()

        if self.funcDefinition or self.funcCall:
            return

        if var not in self.table.keys():
            raise Exception(
                f"Not declared variable '{var}' at {str(ctx.start).removesuffix(']').split(',')[-1]}"
            )


class ListenerDefinitions(Act_31Listener):
    def __init__(self, table):
        self.table = table
        self.defining = False
        self.varible_type = None
        self.funcCall = False
        self.line = None

    def enterDefinition(self, ctx: Act_31Parser.DefinitionContext):
        self.defining = True
        self.line = str(ctx.start).removesuffix("]").split(",")[-1]

    def exitDefinition(self, ctx: Act_31Parser.DefinitionContext):
        self.defining = False
        self.varible_type = None

    def enterFunc_call(self, ctx: Act_31Parser.Func_callContext):
        self.funcCall = True
        if self.defining:
            var = "*" + ctx.getChild(0).getText()
            if self.varible_type != self.table[var]:
                raise Exception(
                    f"Type '{self.table[var]}' from function '{ctx.getChild(0).getText()}' cannot be parsed to type '{self.varible_type}' at line {self.line}"
                )

    def exitFunc_call(self, ctx: Act_31Parser.Func_callContext):
        self.funcCall = False

    # def enterType(self, ctx: Act_31Parser.TypeContext):
    #     self.varible_type = ctx.getText()

    def enterTk_ID(self, ctx: Act_31Parser.Tk_IDContext):
        if self.defining:
            if self.varible_type is None:
                self.varible_type = self.table[ctx.getText()]
            elif not self.funcCall:
                if self.varible_type != self.table[ctx.getText()]:
                    raise Exception(
                        f"Type '{self.table[ctx.getText()]}' from variable {ctx.getText()} cannot be parsed to type '{self.varible_type}' at line {self.line}"
                    )

    def exitTk_int(self, ctx: Act_31Parser.Tk_intContext):
        if self.defining:
            if self.varible_type == "string":
                raise Exception(
                    f"Type 'int' cannot be parsed to type '{self.varible_type}' at line {self.line}"
                )

    def exitTk_float(self, ctx: Act_31Parser.Tk_floatContext):
        if self.defining:
            if self.varible_type != "float":
                raise Exception(
                    f"Type 'float' cannot be parsed to type '{self.varible_type}' at line{self.line}"
                )

    def exitTk_string(self, ctx: Act_31Parser.Tk_stringContext):
        if self.defining:
            if self.varible_type != "string":
                raise Exception(
                    f"Type 'string' cannot be parsed to type '{self.varible_type}' at line {self.line}"
                )
