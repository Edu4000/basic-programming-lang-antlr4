import sys
from antlr4 import *
from ANTLR.AbrilListener import AbrilListener
from ANTLR.AbrilParser import AbrilParser
from ANTLR.AbrilLexer import AbrilLexer
from Listener import Listener

def main(argv):
    parser = AbrilParser(CommonTokenStream(AbrilLexer(FileStream('input.txt'))))
    tree = parser.prog()
    testListener = Listener()

    walker = ParseTreeWalker()
    walker.walk(testListener, tree)

if __name__ == '__main__':
    main(sys.argv)