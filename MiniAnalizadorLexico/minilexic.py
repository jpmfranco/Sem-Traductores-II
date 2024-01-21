def lexer(input_string):
    tokenactual = ""

    for char in input_string:
        if char.isalpha() or char.isdigit() or char == ".":
            if char == '.':
                if tokenactual.count('.') == 0 and tokenactual.count('.') <=1:
                    tokenactual += char
            else:
                tokenactual += char
        else:
            if tokenactual:
                if tokenactual.isdigit():
                    tokenactual = int(tokenactual)
                    print(tokenactual, "\t\tReal")
                else:
                    tokenactual = float(tokenactual) if '.' in tokenactual else print(tokenactual,"\t\tID")
                    if tokenactual == None:
                        tokenactual = ''
                    else:
                        print(tokenactual, "\t\tReal")
                tokenactual = ""


    if tokenactual:
        if tokenactual.isdigit():
            tokenactual = int(tokenactual)
            print(tokenactual, "\t\tReal")
        else:
            tokenactual = float(tokenactual) if '.' in tokenactual else print(tokenactual,"\t\tID")
            if tokenactual == None:
                print("")
            else:
                print(tokenactual, "\t\tReal")


input_text = "entero 98.94 hol123 1982 hola como estas muy bi3n espero+87798+que_987673+muy()bien_987.56"
lexer(input_text)
