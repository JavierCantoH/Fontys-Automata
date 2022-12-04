# antlr -Dlanguage=Python3 -visitor MyGrammar.g4
# antlr -Dlanguage=Python3 MyGrammar.g4 -visitor -o dist 
import sys
from antlr4 import *
from dist.MyGrammarLexer import MyGrammarLexer
from dist.MyGrammarParser import MyGrammarParser
from dist.MyGrammarVisitor import MyGrammarVisitor

class Evaluate(MyGrammarVisitor):
    def visitAtomExpr(self, ctx:MyGrammarParser.AtomExprContext):
        return int(ctx.getText())

    def visitParenExpr(self, ctx:MyGrammarParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitOpExpr(self, ctx:MyGrammarParser.OpExprContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        op = ctx.op.text
        if op == '+':
            return l + r
        elif op == '-':
            return l - r
        elif op == '*':
            return l * r
        elif op == '/':
            if r == 0:
                print('divide by zero!')
                return 0
            return l / r
 
def main(argv) -> float:
    #input_stream = FileStream("input.txt")
    input_stream = InputStream(argv)
    lexer = MyGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(stream)
    tree = parser.expr()
    visitor = Evaluate()
    return visitor.visit(tree)

if __name__ == '__main__':    
    while True:
        print("New line to evaluate: ", end='')
        argv = input()
        print(main(argv))