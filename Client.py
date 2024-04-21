import sys
from antlr4 import *
from Grammar.Act_31Listener import Act_31Listener
from Grammar.Act_31Parser import Act_31Parser
from Grammar.Act_31Lexer import Act_31Lexer
from Listener import Listener, ListenerDefinitions


def main(argv):
    parser = Act_31Parser(CommonTokenStream(Act_31Lexer(FileStream("input.txt"))))
    tree = parser.prog()
    walker = ParseTreeWalker()

    testListener = Listener()
    walker.walk(testListener, tree)

    definitionListener = ListenerDefinitions(testListener.table)
    walker.walk(definitionListener, tree)


if __name__ == "__main__":
    main(sys.argv)
