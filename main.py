from classes.Lexical import Lexical
from classes.Syntactic import Syntactic
def main():
    linea = input()
    l = Lexical()
    tokenList, tokenValid = l.matrixHandler(linea)
    if tokenValid:
        s = Syntactic(tokenList)
        s.syntacticAnalysis()

if __name__== "__main__":
    main()