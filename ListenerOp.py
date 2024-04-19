from ANTLR.AbrilListener import  AbrilListener
from ejemplosANTLR.abril.ANTLR.AbrilParser import AbrilParser


class Listener(AbrilListener):

    def __init__(self, table):
        self.table = table
        pass

    def exitSum(self, ctx:AbrilParser.SumContext):
        left = ctx.getChild(0).type
        right = ctx.getChild(1).type

        if left != right:
            raise Exception("Different types")

        ctx.type = left

    def exitVar(self, ctx:AbrilParser.VarContext):
        ctx.type = self.table[ctx.getText()]

    def exitInt(self, ctx:AbrilParser.IntContext):
        ctx.type = 'int'

    def exitFloat(self, ctx:AbrilParser.FloatContext):
        ctx.type = 'float'

    def exitString(self, ctx:AbrilParser.StringContext):
        ctx.type = 'str'

