from .Token import Token

class Syntactic:
    def __init__(self, tokenList):
        self.tokenList = tokenList

    def syntacticAnalysis(self):
        if (self.tokenList and self.recursiveDescent()):
            print("The input es a well formed expression.\n")
        else:
            print("SYNTACTIC ERROR: The expression is not valid.\n")

    def recursiveDescent(self):
        valid = True
        valid = self.match(Token("Parenthesis", "("), True)
        if (valid):
            valid = self.parseBody()
        if (valid):
            valid = self.match(Token("Parenthesis", ")"), True)
        return valid

    def match(self, correct_token, exact):
        actual_token = self.tokenList[0]
        actual_type, actual_value = actual_token.getElements()
        if actual_type == correct_token.type:
            if exact:
                if actual_value == correct_token.value:
                    self.tokenList.pop(0)
                    return True
                else:
                    return False
            self.tokenList.pop(0)
            return True
        return False

    def parseBody(self):
        valid = self.parseOperator()
        if valid:
            valid = self.parseVarNum()
        if valid:
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
