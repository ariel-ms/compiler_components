from classes.Lexical import Lexical
def main():
    # file = open("file.txt", "r")
    # lineas = file.readlines()
    lineas = ")"
    # print(lineas)
    # file.close()
    # linea = input()
    # print(len(linea))
    l = Lexical()
    tokens = l.matrixHandler(lineas)
    for token in tokens:
        print(token)
    



  
if __name__== "__main__":
    main()