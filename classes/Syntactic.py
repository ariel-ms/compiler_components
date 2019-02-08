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
        valid = self.match(Token("Parenthesis", "("), True) #create match
        if (valid):
            valid = self.parseBody(self.tokensList)
        if (valid):
            valid = self.match(Token("Parenthesis", ")"), True)
        return valid

    def match(self, correct_token, exact):
        actual_token = self.tokenList[0]
        actual_type, actual_value = actual_token.getElements()
        if actual_type == correct_token.type:
            if exact:
                if actual_value == correct_token.value:
                    self.tokenList = self.tokenList[1:]
                    return True
                else:
                    return False
            self.tokenList = self.tokenList[1:]
            return True
        return False

    def parseBody(self, tokenList):
        valid = self.parseOperator()
        valid = self.parseVarNum() # meter ifs en caso de que sea falso
        valid = self.parseVarNum()
        return valid

    def parseOperator(self):
        return self.match(Token("Operator", ""), False)

    def parseVarNum(self):
        actual_token = self.tokenList[0]
        actual_value = actual_token.value
        if actual_value == "(":
            self.match(Token("Parenthesis", "("), True)
            self.parseOperator()
            self.match(Token("Parenthesis", ")"), True)
        elif self.match(Token("Variable", ""), False):
            return True
        elif self.match(Token("Number", ""), False):
            return True
        return False
