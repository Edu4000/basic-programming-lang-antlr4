from Grammar.Act_31Listener import Act_31Listener
from Grammar.Act_31Parser import Act_31Parser


class Listener(Act_31Listener):

    def __init__(self):
        self.table = {}

    # Creating reference table
    def enterDeclaration(self, ctx: Act_31Parser.DeclarationContext):
        type = ctx.getChild(0).getText()
        var = ctx.getChild(1).getText()

        if var in self.table.keys():
            raise Exception("Duplicate declaration")
        else:
            self.table[var] = type

    # Makins sure variable reference exists
    def enterTk_ID(self, ctx: Act_31Parser.Tk_IDContext):
        var = ctx.getChild(0).getText()

        if var not in self.table.keys():
            raise Exception("Not declared variable at", ctx.getText())


class ListenerDefinitions(Act_31Listener):

    def __init__(self, table):
        self.table = table
        self.defining = False
        self.varible_type = None

    def enterDefinition(self, ctx: Act_31Parser.DefinitionContext):
        self.defining = True

    def exitDefinition(self, ctx: Act_31Parser.DefinitionContext):
        self.defining = False

    def enterTk_ID(self, ctx: Act_31Parser.Tk_IDContext):
        if self.defining:
            # print(ctx.getText(), " | ", self.table[ctx.getText()])
            self.varible_type = self.table[ctx.getText()]

    # def exitSum(self, ctx: Act_31Parser.SumContext):
    #     left = ctx.getChild(0).type
    #     right = ctx.getChild(1).type

    #     if left != right:
    #         raise Exception("Different types")

    #     ctx.type = left

    # def exitVar(self, ctx: Act_31Parser.VarContext):
    #     ctx.type = self.table[ctx.getText()]

    # def exitInt(self, ctx: Act_31Parser.IntContext):
    #     ctx.type = "int"

    # def exitFloat(self, ctx: Act_31Parser.FloatContext):
    #     ctx.type = "float"

    # def exitString(self, ctx: Act_31Parser.StringContext):
    #     ctx.type = "str"
