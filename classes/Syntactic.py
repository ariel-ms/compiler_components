from .Lexical import Token

class Syntactic:
    def __init__(self):
        self.tokenList = []

    def syntacticAnalysis(self, string):
        l = Lexical()
        self.tokensList = l.matrixHandler(string)

        if (self.recursiveDescent()):
            print("The input es a well formed expression.\n")
        else:
            print("SYNTACTIC ERROR: The expression is not valid.\n")

    def recursiveDescent(self):
        valid = true
        valid = match("(", self.tokensList) #create match
        if (valid):
            valid = parseBody(self.tokensList)
        if (valid):
            valid = match(")", self.tokensList)
        return valid

    def match ():
        #do some shit
        self.tokenList = self.tokenList[1:]
