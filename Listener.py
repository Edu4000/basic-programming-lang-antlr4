from ANTLR.AbrilListener import AbrilListener
from ejemplosANTLR.abril.ANTLR.AbrilParser import AbrilParser


class Listener(AbrilListener):

    def __init__(self):
        self.table = {}
        pass

    def enterDeclaration(self, ctx:AbrilParser.DeclarationContext):
        type = ctx.getChild(0).getText()
        var = ctx.getChild(1).getText()

        if (var in self.table.keys()):
            raise Exception("Duplicate declaration")
        else:
            self.table[var] = type

    def enterVar(self, ctx:AbrilParser.VarContext):
        var = ctx.getChild(0).getText()

        if (var not in self.table.keys()):
            raise Exception("Not declared variable")