#Test case 1: (+ 4 10 )  Correct
#Test case 1: (+ 4 10)   Lexical error
#Test case 1: (+ 10 )    Syntactic error
#Test case 1: (+ 4 $vala )  Correct

from classes.Lexical import Lexical
from classes.Syntactic import Syntactic
def main():
    print ("String? ", end = '')
    linea = input()
    l = Lexical()
    tokenList, tokenValid = l.matrixHandler(linea)
    if tokenValid:
        s = Syntactic(tokenList)
        s.syntacticAnalysis()

if __name__== "__main__":
    main()