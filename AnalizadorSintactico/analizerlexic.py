class Lexico:
    def __init__(self,cadena):
        self.ind = 0
        self.estado = 0
        self.tipo = 0
        self.car = 'd'
        self.continuar = True
        self.token = ""
        self.simbolo = ""
        self.cadena = cadena

    def entrada(self, cadena):
        self.ind = 0
        self.cadena = cadena + "$"

    def sigcar(self):
        if self.ind < len(self.cadena):
            caracter = self.cadena[self.ind]
            self.ind += 1
            return caracter
        else:
            return '$'

    def regresar(self):
        self.continuar = False
        self.ind -= 1
    
    def isDigit(self):
        return self.car.isdigit()
    
    def isCaracter(self):
        return self.car.isalpha()

    def cambioestado(self):
        self.estado = 0
        self.continuar = True
        self.token = ""
        self.tipo = -1
        self.simbolo = ""

        while self.continuar:
            self.car = self.sigcar()
            match self.estado:
                case 0:
                    if self.car == "i":
                        self.estado = 12
                        self.token = self.token + self.car
                    elif self.car == "w":
                        self.estado = 16
                        self.token = self.token + self.car
                    elif self.car == "r":
                        self.estado = 21
                        self.token = self.token + self.car
                    elif self.car == "e":
                        self.estado = 27
                        self.token = self.token + self.car
                    elif self.car == "f":
                        self.estado = 31
                        self.token = self.token + self.car
                    elif self.car == "v":
                        self.estado = 36
                        self.token = self.token + self.car
                    elif self.isDigit():
                        self.estado = 3
                        self.token = self.token + self.car
                    elif self.isCaracter():
                        self.estado = 1
                        self.token = self.token + self.car
                    elif self.car == "+" or self.car == "-":
                        self.token += self.car
                        self.continuar = False
                        self.tipo = 5
                        self.simbolo = "OpSuma"
                    elif self.car == "=":
                        self.estado = 7
                        self.token = self.token + self.car
                    elif self.car == "<" or self.car == ">":
                        self.estado = 8
                        self.token = self.token + self.car
                    elif self.car == "&":
                        self.estado = 9
                        self.token = self.token + self.car
                    elif self.car == "|":
                        self.estado = 10
                        self.token = self.token + self.car
                    elif self.car == "!":
                        self.estado = 11
                        self.token = self.token + self.car
                    elif self.car == "(" or self.car == ")":
                        if self.car == "(":
                            self.token += self.car
                            self.continuar = False
                            self.tipo = 14
                            self.simbolo = "Parentesis"
                        else:
                            self.token += self.car
                            self.continuar = False
                            self.tipo = 15
                            self.simbolo = "Parentesis"
                    elif self.car == "{" or self.car == "}":
                        if self.car == "{":
                            self.token += self.car
                            self.continuar = False
                            self.tipo = 16
                            self.simbolo = "Llave"
                        else:
                            self.token += self.car
                            self.continuar = False
                            self.tipo = 17
                            self.simbolo = "Llave"
                    elif self.car == ";":
                        self.token += self.car
                        self.continuar = False
                        self.tipo = 12
                        self.simbolo = "PuntoyComa"
                    elif self.car == ",":
                        self.token += self.car
                        self.continuar = False
                        self.tipo = 13
                        self.simbolo = "Coma"
                    elif self.car == "*" or self.car == "/":
                        self.token += self.car
                        self.continuar = False
                        self.tipo = 6
                        self.simbolo = "OpMul"
                    elif self.car == "$":
                        self.token += self.car
                        self.continuar = False
                        self.tipo = 23
                        self.simbolo = "$"
                        

                case 1:  # Identificador
                    self.simbolo = "ID"
                    if self.isDigit() or self.isCaracter():
                        self.token = self.token + self.car

                    elif self.car == "$" or self.car == " ":
                        self.continuar = False
                        self.tipo = 0
                        self.simbolo = "ID"
                    else:
                        self.regresar()
                        self.tipo = 0
                        self.simbolo = "ID"

                case 2:  # Cadena
                    if self.isCaracter():
                        self.token = self.token + self.car
                    
                    elif self.isDigit() or self.car == ".":
                        self.estado = 3
                        self.token = self.token + self.car

                    elif self.car == "$" or self.car == " ":
                        self.continuar = False
                        self.tipo = 3
                        self.simbolo = "Cadena"
                    else:
                        self.regresar()
                        self.tipo = 3
                        self.simbolo = "Cadena"

                case 3:#Entero
                    if self.isDigit():
                        self.token = self.token + self.car
                    elif self.car == ".":
                        self.estado = 5
                        self.token = self.token + self.car
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 1
                        self.simbolo = "Entero"
                    else:
                        self.regresar()
                        self.tipo = 1
                        self.simbolo = "Entero"

                case 4:  # Cadenas error
                    if self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = -1
                        self.simbolo = "Error"
                    else:
                        self.token = self.token + self.car

                case 5:  # Reales
                    if self.isDigit():
                        self.token = self.token + self.car
                        self.estado = 6
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = -1
                        self.simbolo = "Error"
                    else:
                        self.regresar()
                        self.tipo = -1
                        self.simbolo = "Error"

                case 6:  # Reales continuación de enteros
                    if self.isDigit():
                        self.token = self.token + self.car
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 2
                        self.simbolo = "Real"
                    else:
                        self.regresar()
                        self.tipo = 2
                        self.simbolo = "Real"

                case 7:  # Igual o doble igual
                    if self.car == "=":
                        self.token = self.token + self.car
                        self.continuar = False
                        self.tipo = 11
                        self.simbolo = "Opigualdad"
                    elif self.car == " " or self.car == "$":
                       
                        self.continuar = False
                        self.tipo = 18
                        self.simbolo = "Igual"
                    else:
                        self.regresar()
                        self.tipo = 18
                        self.simbolo = "Igual"

                case 8:  # Relacionales < > <= >=
                    if self.car == "=":
                        self.token = self.token + self.car
                        self.continuar = False
                        self.tipo = 7
                        self.simbolo = "OpRelac"
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 7
                        self.simbolo = "OpRelac"
                    else:
                        self.regresar()
                        self.tipo = 7
                        self.simbolo = "OpRelac"

                case 9:  # And
                    if self.car == "&":
                        self.token = self.token + self.car
                        self.continuar = False
                        self.tipo = 9
                        self.simbolo = "OpAnd"
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = -1
                        self.simbolo = "Error"
                    else:
                        self.regresar()
                        self.tipo = -1
                        self.simbolo = "Error"

                case 10:  # Or
                    if self.car == "|":
                        self.token = self.token + self.car
                        self.continuar = False
                        self.tipo = 9
                        self.simbolo = "OpOr"
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = -1
                        self.simbolo = "Error"
                    else:
                        self.regresar()
                        self.tipo = -1
                        self.simbolo = "Error"

                case 11:  # Not o igualdad
                    if self.car == "=":
                        self.token = self.token + self.car
                        self.continuar = False
                        self.tipo = 11
                        self.simbolo = "OpIgualdad"
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 10
                        self.simbolo = "OpNot"
                    else:
                        self.regresar()
                        self.tipo = 10
                        self.simbolo = "OpNot"

                case 12:  # f (if) o n (int)
                    if self.car == "f":
                        self.token = self.token + self.car
                        self.estado = 13
                    elif self.car == "n":
                        self.token = self.token + self.car
                        self.estado = 14
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 0
                        self.simbolo = "ID"
                    else:
                        self.ind -= 1
                        self.estado = 1

                case 13:  # checar si if es reservada o identificador
                    if self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 19
                        self.simbolo = "if"
                    elif self.isCaracter() or self.isDigit():
                        self.token = self.token + self.car
                        self.estado = 1
                    else:
                        self.regresar()
                        self.tipo = 19
                        self.simbolo = "if"

                case 14:  # int
                    if self.car == "t":
                        self.token = self.token + self.car
                        self.estado = 15
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 0
                        self.simbolo = "ID"
                    else:
                        self.ind -= 1
                        self.estado = 1

                case 15:  # checar si int es reservada o identificador
                    if self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 4
                        self.simbolo = "Tipo"
                    elif self.isCaracter() or self.isDigit():
                        self.token = self.token + self.car
                        self.estado = 1
                    else:
                        self.regresar()
                        self.tipo = 4
                        self.simbolo = "Tipo"

                case 16:  # W (hile)
                    if self.car == "h":
                        self.token = self.token + self.car
                        self.estado = 17
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 0
                        self.simbolo = "ID"
                    else:
                        self.ind -= 1
                        self.estado = 1

                case 17:  # Wh (ile)
                    if self.car == "i":
                        self.token = self.token + self.car
                        self.estado = 18
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 0
                        self.simbolo = "ID"
                    else:
                        self.ind -= 1
                        self.estado = 1

                case 18:  # Whi (le)
                    if self.car == "l":
                        self.token = self.token + self.car
                        self.estado = 19
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 0
                        self.simbolo = "ID"
                    else:
                        self.ind -= 1
                        self.estado = 1

                case 19:  # Whil (e)
                    if self.car == "e":
                        self.token = self.token + self.car
                        self.estado = 20
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 0
                        self.simbolo = "ID"
                    else:
                        self.ind -= 1
                        self.estado = 1

                case 20:  # checar si while es reservada o identificador
                    if self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 20
                        self.simbolo = "while"
                    elif self.isCaracter() or self.isDigit():
                        self.token = self.token + self.car
                        self.estado = 1
                    else:
                        self.regresar()
                        self.tipo = 20
                        self.simbolo = "while"

                case 21:  # r (eturn)
                    if self.car == "e":
                        self.token = self.token + self.car
                        self.estado = 22
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 0
                        self.simbolo = "ID"
                    else:
                        self.ind -= 1
                        self.estado = 1

                case 22:  # re (turn)
                    if self.car == "t":
                        self.token = self.token + self.car
                        self.estado = 23
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 0
                        self.simbolo = "ID"
                    else:
                        self.ind -= 1
                        self.estado = 1

                case 23:  # ret (urn)
                    if self.car == "u":
                        self.token = self.token + self.car
                        self.estado = 24
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 0
                        self.simbolo = "ID"
                    else:
                        self.ind -= 1
                        self.estado = 1

                case 24:  # retu (rn)
                    if self.car == "r":
                        self.token = self.token + self.car
                        self.estado = 25
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 0
                        self.simbolo = "ID"
                    else:
                        self.ind -= 1
                        self.estado = 1

                case 25:  # retur (n)
                    if self.car == "n":
                        self.token = self.token + self.car
                        self.estado = 26
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 0
                        self.simbolo = "ID"
                    else:
                        self.ind -= 1
                        self.estado = 1

                case 26:  # checar si return es reservada o identificador
                    if self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 21
                        self.simbolo = "return"
                    elif self.isCaracter() or self.isDigit():
                        self.token = self.token + self.car
                        self.estado = 1
                    else:
                        self.regresar()
                        self.tipo = 21
                        self.simbolo = "return"

                case 27:  # e (lse)
                    if self.car == "l":
                        self.token = self.token + self.car
                        self.estado = 28
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 0
                        self.simbolo = "ID"
                    else:
                        self.ind -= 1
                        self.estado = 1

                case 28:  # el (se)
                    if self.car == "s":
                        self.token = self.token + self.car
                        self.estado = 29
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 0
                        self.simbolo = "ID"
                    else:
                        self.ind -= 1
                        self.estado = 1

                case 29:  # els (e)
                    if self.car == "e":
                        self.token = self.token + self.car
                        self.estado = 30
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 0
                        self.simbolo = "ID"
                    else:
                        self.ind -= 1
                        self.estado = 1

                case 30:  # checar si else es reservada o identificador
                    if self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 22
                        self.simbolo = "else"
                    elif self.isCaracter() or self.isDigit():
                        self.token = self.token + self.car
                        self.estado = 1
                    else:
                        self.regresar()
                        self.tipo = 22
                        self.simbolo = "else"

                case 31:  # f (loat)
                    if self.car == "l":
                        self.token = self.token + self.car
                        self.estado = 32
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 0
                        self.simbolo = "ID"
                    else:
                        self.ind -= 1
                        self.estado = 1

                case 32:  # fl (oat)
                    if self.car == "o":
                        self.token = self.token + self.car
                        self.estado = 33
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 0
                        self.simbolo = "ID"
                    else:
                        self.ind -= 1
                        self.estado = 1

                case 33:  # flo (at)
                    if self.car == "a":
                        self.token = self.token + self.car
                        self.estado = 34
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 0
                        self.simbolo = "ID"
                    else:
                        self.ind -= 1
                        self.estado = 1

                case 34:  # floa (t)
                    if self.car == "t":
                        self.token = self.token + self.car
                        self.estado = 35
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 0
                        self.simbolo = "ID"
                    else:
                        self.ind -= 1
                        self.estado = 1

                case 35:  # checar si float es tipo o identificador
                    if self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 4
                        self.simbolo = "Tipo"
                    elif self.isCaracter() or self.isDigit():
                        self.token = self.token + self.car
                        self.estado = 1
                    else:
                        self.regresar()
                        self.tipo = 4
                        self.simbolo = "Tipo"

                case 36:  # v (oid)
                    if self.car == "o":
                        self.token = self.token + self.car
                        self.estado = 37
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 0
                        self.simbolo = "ID"
                    else:
                        self.ind -= 1
                        self.estado = 1

                case 37:  # vo (id)
                    if self.car == "i":
                        self.token = self.token + self.car
                        self.estado = 38
                    elif self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 0
                        self.simbolo = "ID"
                    else:
                        self.ind -= 1
                        self.estado = 1

                case 38:  # voi (d)
                    if self.car == "d":
                        self.token = self.token + self.car
                        self.estado = 39

                case 39:  # checar si void es tipo o identificador
                    if self.car == " " or self.car == "$":
                        self.continuar = False
                        self.tipo = 4
                        self.simbolo = "Tipo"
                    elif self.isCaracter() or self.isDigit():
                        self.token = self.token + self.car
                        self.estado = 1
                    else:
                        self.regresar()
                        self.tipo = 4
                        self.simbolo = "Tipo"
                        



                


#cadena = "juan como123 7.8909+123 +-*/==!=!<><=float>=int()if{,}while;while1234=return-&&&|||$"
#lex = Lexico(cadena)
#print("Resultado del analisis lexico:")
#print("Palabra\t        ||   Simbolo\t||\tTipo     ||")
#print("====================================================")
#while lex.car != '$':
#    lex.cambioestado()
#    if len(lex.simbolo) <= 7 and len(lex.token) <= 7:
#        print(f"{lex.token}\t\t||\t{lex.simbolo}\t||\t{lex.tipo}\t||"#
#
#   else:
#       if len(lex.token) <= 7:
#            print(f"{lex.token}\t\t||  {lex.simbolo}\t||\t{lex.tipo}\t||") 
#       else:
#           print(f"{lex.token}\t|| \t{lex.simbolo}\t||\t{lex.tipo}\t||") 
           
#input("\nPrograma terminado, presiona enter para terminar")
