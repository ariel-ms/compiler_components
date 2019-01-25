class Lexical:
    def __init__(self):
        self.ERROR = 999
        # columns: digit, space, letter, $, parentesis, operadores
        self.transitionMatrix = [[1, 0, self.ERROR, 2, 103, 104], \
                                [1, 101, self.ERROR, self.ERROR, self.ERROR, self.ERROR],\
                                [3, self.ERROR, self.ERROR, self.ERROR, self.ERROR, self.ERROR], \
                                [3, 102, 3, self.ERROR, self.ERROR, self.ERROR]]

    def matrixHandler(self, linea):
        value = ""
        index = 0
        state = 0
        while index < len(linea) and state < 100:
            c = linea[index]
            state = self.transitionMatrix[state][self.filter(c)]
            if c != 0:
                value += c
            index += 1
        return value

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
            return 2
        elif char in ["+", "-", "*", "/"]:
            return 5
        else:
            return 6