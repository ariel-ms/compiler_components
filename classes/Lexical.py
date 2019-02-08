from .Token import Token

#(345+43)*4

class Lexical:
    def __init__(self):
        self.ERROR = 999
        # columns: digit, space, letter, $, parentesis, operadores
        self.transitionMatrix = [[1, 0, self.ERROR, 2, 103, 104], \
                                [1, 101, self.ERROR, self.ERROR, self.ERROR, self.ERROR],\
                                [self.ERROR, self.ERROR, 3, self.ERROR, self.ERROR, self.ERROR], \
                                [3, 102, 3, self.ERROR, self.ERROR, self.ERROR]]
        self.type_dict = {101: "Number", 102: "Variable", 103: "Parenthesis", 104: "Operator"}

    def matrixHandler(self, linea):
        index = state = 0
        token_list = []
        valid = True
        while index < len(linea) and state != self.ERROR:
            value = ""
            state = 0
            while index < len(linea) and state < 100:
                char = linea[index]
                state = self.transitionMatrix[state][self.filter(char)]
                if state != 0:
                    value += char
                index += 1
            if state != self.ERROR:
                if state == 1:
                    state = 101
                elif state == 3:
                    state = 102
                token_list.append(Token(self.type_dict.get(state), value))
            else:
                print("LEXICAL ERROR: the string " + value + " is not a valid element in the language.")
                valid = False
            value = ""
        return token_list, valid

    def filter(self, char):
        if char.isdigit():
            return 0
        elif char == " ":
            return 1
        elif char.isalpha():
            return 2
        elif char == "$":
            return 3
        elif char == "(" or char == ")":
            return 4
        elif char in ["+", "-", "*", "/"]:
            return 5
        else:
            return 6
