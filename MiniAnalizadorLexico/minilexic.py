def lexer(input_string):
    tokenactual = ""

    
    for char in input_string:
        if char.isalpha() or char.isdigit() or char == ".":
            if char == '.':
                tokenactual += int(char)
            else:
                tokenactual += char
        else:
            if tokenactual:
                if tokenactual.isdigit():
                    tokenactual = int(tokenactual)
                    print(tokenactual,"\t\tReal")
                elif tokenactual.isdigit() and tokenactual :
                    print(tokenactual,"\t\tReal")
                else:
                    print(tokenactual,"    \tID")
                tokenactual = ""

    if tokenactual:
        if tokenactual.isdigit():
            tokenactual = int(tokenactual)
            print(tokenactual,"\tEntero")
        else:
            print(tokenactual," \t\tID")


# Ejemplo de uso
input_text = "entero 98.90 hola123  1982 hola como estas muy bi3n espero+87798+que_987673+muy()bien"
lexer(input_text)
