from .Lexical import Lexical
from .Token import Token

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
        valid = True
        valid = self.match(Token("Parenthesis", "(")) #create match
        if (valid):
            valid = self.parseBody(self.tokensList)
        if (valid):
            valid = self.match(Token("Parenthesis", ")"))
        return valid

    def match(self, correct_token):
        actual_token = self.tokenList[0]
        actual_type, actual_value = actual_token.getElements()
        if actual_type == correct_token.type and actual_value == correct_token.value:
            self.tokenList = self.tokenList[1:]
            return True
        return False

    def parseBody(self, tokenList):
        return False
