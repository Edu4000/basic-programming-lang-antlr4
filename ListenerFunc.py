from ANTLR.AbrilListener import  AbrilListener
from ejemplosANTLR.abril.ANTLR.AbrilParser import AbrilParser


class Listener(AbrilListener):

    def __init__(self, table):
        self.table = table
        self.type = ''
        pass

    def exitFunc_type(self, ctx:AbrilParser.Func_typeContext):
        self.type = ctx.getText()

    def enterReturn(self, ctx:AbrilParser.ReturnContext):
        if ctx.getChild(1).getText() != self.type:
            raise Exception("Expected " + self.type + " but got " + ctx.getChild(1).getText())