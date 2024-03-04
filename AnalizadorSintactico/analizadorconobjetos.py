import analizerlexic as lexico

class ElementoPila:
    def __init__(self):
        self.token = ""
    
    def getToken(self):
        return self.token
    
    def set_token(self, tokens):
        self.token = tokens
    
    def print_token(self, nivel):
        print(" " * nivel + self.token)
    
    def get_nodo(self):
        return []
    
    def get_tipo(self):
        return -1

class Terminal(ElementoPila):
    def __init__(self, tokens):
        super().set_token(tokens)
        self.tipo = -1
    
    def set_tipo(self, tip):
        self.tipo = tip
    
    def get_tipo(self):
        return self.tipo

class NoTerminal(ElementoPila):
    def __init__(self, tokens):
        super().set_token(tokens)
        self.nodo = []
    
    def push_nodo(self, elemento):
        self.nodo.append(elemento)
    
    def print_token(self, nivel):
        print(" " * nivel + self.get_token() + " -")
        while self.nodo:
            self.nodo[-1].print_token(nivel + 1)
            self.nodo.pop()
    
    def get_nodo(self):
        return self.nodo

class Estado(ElementoPila):
    def __init__(self, tokens):
        super().__init__()
        self.set_token(tokens)

class Sintactico:
    def __init__(self):
        self.pila = []
        self.LR = [46 * [""], 95 * [""]]
        self.llenarLR()

    def empezar(self):
        self.pila.append(Terminal("$"))
        self.pila.append(Estado("0"))

    def getLRAt(self, fila, columna):
        return self.LR[fila][columna]

    def llenarLR(self):
        try:
            with open("compilador.csv", "r") as fin:
                entro = False
                firstline = True
                firstword = True
                fila = 0
                columna = 0
                for line in fin:
                    if firstline:
                        firstline = False
                    else:
                        entro = True
                        words = line.strip().split(",")
                        for word in words:
                            if firstword:
                                firstword = False
                            else:
                                self.LR[fila][columna] = word
                                columna += 1
                        firstword = True
                        columna = 0
                        fila += 1
                return entro
        except FileNotFoundError:
            return False

    def printLR(self):
        for i in range(95):
            for j in range(46):
                if self.getLRAt(i, j) == "":
                    print("v ", end="")
                else:
                    print(self.getLRAt(i, j) + " ", end="")
            print()

    def popPila(self):
        self.pila.pop()

    def pilaTop(self):
        if self.pila:
            return self.pila[-1]
        else:
            return None

    def salida(self, tokens, tipo):
        if tipo < 0 or tipo > 46:
            return ""
        fila = int(self.pilaTop().getToken())
        if fila < 0 or fila > 94:
            return ""
        estado = self.getLRAt(fila, tipo)
        if estado == "r0":
            return estado
        elif estado[0] == "d":
            t = Terminal(tokens)
            t.setTipo(tipo)
            self.pila.append(t)
            self.pila.append(Estado(estado[1:]))
            return estado
        elif estado[0] == "r":
            numregla = int(estado[1:])
            retorno = ""
            if numregla == 1:
                retorno = self.regla(1, 24, estado, "Programa")
            elif numregla == 2:
                retorno = self.regla(0, 25, estado, "Definiciones")
            elif numregla == 3:
                retorno = self.regla(2, 25, estado, "Definiciones")
            elif numregla == 4:
                retorno = self.regla(1, 26, estado, "Definicion")
            elif numregla == 5:
                retorno = self.regla(1, 26, estado, "Definicion")
            elif numregla == 6:
                retorno = self.regla(4, 27, estado, "DefVar")
            elif numregla == 7:
                retorno = self.regla(0, 28, estado, "ListaVar")
            elif numregla == 8:
                retorno = self.regla(3, 28, estado, "ListaVar")
            elif numregla == 9:
                retorno = self.regla(6, 29, estado, "DefFunc")
            elif numregla == 10:
                retorno = self.regla(0, 30, estado, "Parametros")
            elif numregla == 11:
                retorno = self.regla(3, 30, estado, "Parametros")
            elif numregla == 12:
                retorno = self.regla(0, 31, estado, "ListaParam")
            elif numregla == 13:
                retorno = self.regla(4, 31, estado, "ListaParam")
            elif numregla == 14:
                retorno = self.regla(3, 32, estado, "BloqFunc")
            elif numregla == 15:
                retorno = self.regla(0, 33, estado, "DefLocales")
            elif numregla == 16:
                retorno = self.regla(2, 33, estado, "DefLocales")
            elif numregla == 17:
                retorno = self.regla(1, 34, estado, "DefLocal")
            elif numregla == 18:
                retorno = self.regla(1, 34, estado, "DefLocal")
            elif numregla == 19:
                retorno = self.regla(0, 35, estado, "Sentencias")
            elif numregla == 20:
                retorno = self.regla(2, 35, estado, "Sentencias")
            elif numregla == 21:
                retorno = self.regla(4, 36, estado, "Sentencia")
            elif numregla == 22:
                retorno = self.regla(6, 36, estado, "Sentencia")
            elif numregla == 23:
                retorno = self.regla(5, 36, estado, "Sentencia")
            elif numregla == 24:
                retorno = self.regla(3, 36, estado, "Sentencia")
            elif numregla == 25:
                retorno = self.regla(2, 36, estado, "Sentencia")
            elif numregla == 26:
                retorno = self.regla(0, 37, estado, "Otro")
            elif numregla == 27:
                retorno = self.regla(2, 37, estado, "Otro")
            elif numregla == 28:
                retorno = self.regla(3, 38, estado, "Bloque")
            elif numregla == 29:
                retorno = self.regla(0, 39, estado, "ValorRegresa")
            elif numregla == 30:
                retorno = self.regla(1, 39, estado, "ValorRegresa")
            elif numregla == 31:
                retorno = self.regla(0, 40, estado, "Argumentos")
            elif numregla == 32:
                retorno = self.regla(2, 40, estado, "Argumentos")
            elif numregla == 33:
                retorno = self.regla(0, 41, estado, "ListaArgumentos")
            elif numregla == 34:
                retorno = self.regla(3, 41, estado, "ListaArgumentos")
            elif numregla == 35:
                retorno = self.regla(1, 42, estado, "Termino")
            elif numregla == 36:
                retorno = self.regla(1, 42, estado, "Termino")
            elif numregla == 37:
                retorno = self.regla(1, 42, estado, "Termino")
            elif numregla == 38:
                retorno = self.regla(1, 42, estado, "Termino")
            elif numregla == 39:
                retorno = self.regla(1, 42, estado, "Termino")
            elif numregla == 40:
                retorno = self.regla(4, 43, estado, "LlamadaFunc")
            elif numregla == 41:
                retorno = self.regla(1, 44, estado, "SentenciaBloque")
            elif numregla == 42:
                retorno = self.regla(1, 44, estado, "SentenciaBloque")
            elif numregla == 43:
                retorno = self.regla(3, 45, estado, "Expresion")
            elif numregla == 44:
                retorno = self.regla(2, 45, estado, "Expresion")
            elif numregla == 45:
                retorno = self.regla(2, 45, estado, "Expresion")
            elif numregla == 46:
                retorno = self.regla(3, 45, estado, "Expresion")
            elif numregla == 47:
                retorno = self.regla(3, 45, estado, "Expresion")
            elif numregla == 48:
                retorno = self.regla(3, 45, estado, "Expresion")
            elif numregla == 49:
                retorno = self.regla(3, 45, estado, "Expresion")
            elif numregla == 50:
                retorno = self.regla(3, 45, estado, "Expresion")
            elif numregla == 51:
                retorno = self.regla(3, 45, estado, "Expresion")
            elif numregla == 52:
                retorno = self.regla(1, 45, estado, "Expresion")
            return retorno
        elif estado == "":
            return ""
        else:
            return estado

    def regla(self, elementos, columna, estad, nomRegla):
        nt = NoTerminal(nomRegla)
        for i in range(elementos * 2):
            if i % 2 == 1:
                nt.pushNodo(self.pilaTop())
            self.popPila()
        fila = int(self.pilaTop().getToken())
        estado = self.getLRAt(fila, columna)
        if estado == "":
            return ""
        else:
            self.pila.append(nt)
            self.pila.append(Estado(estado))
            return estad[1:] + "-e"

    def getPilaSize(self):
        return len(self.pila)

    def pilaToString(self):
        pilaEntera = ""
        for elem in self.pila[::-1]:
            pilaEntera += elem.getToken()
        return pilaEntera




# Assuming Lexico and Sintactico are classes that have been defined in Python
# with equivalent functionality to their C++ counterparts.

with open("D:\pablo\Documents\sexto semestre\Sem Traductores II\AnalizadorSintactico\codigo.txt", 'r') as file:
    cadena = file.read()
lexico = lexico.Lexico(cadena)
sintactico = Sintactico()
lexico.entrada(cadena)
print("Estado en pila\t||\tEntrada\t\t||\tSalida")
print("======================================================")
lexicoFlag = True
entradaSint = lexico.getCadenaFromInd()
back = sintactico.pilaTop().getToken()
lexico.cambioestado()
salida = sintactico.salida(lexico.token, lexico.tipo)
while salida != -199:
    if lexico.tipo < 0:
        lexicoFlag = False
    if salida < -199:
        print(f"{back}\t\t\t{entradaSint}$\t\tError")
        print("Resultado del analisis sintactico: Error")
        break
    elif salida < 0:
        if len(entradaSint) >= 7:
            print(f"\t{back}\t||\t\t{entradaSint}$\t||\tr{abs(salida)}")
        else:
            print(f"\t{back}\t||\t{entradaSint}$ \t\t||\t r{abs(salida)}")
    else:
        if len(entradaSint) >= 7:
            print(f"\t{back}\t||\t{entradaSint}$\t||\td{salida}")
        else:
            print(f"\t{back}\t||\t{entradaSint}$\t\t||\td{salida}")
    entradaSint = lexico.getCadenaFromInd()
    back = sintactico.pilaTop().get_token()
    lexico.cambioestado()
    salida = sintactico.salida(lexico.token, lexico.tipo)
if salida == -199:
    print(f"\t{back}\t||\t{entradaSint}$\t\t||\tr0 (acept)")
    print("Resultado del analisis sintactico: Correcto")
    print("==============================================================")
    print("Resultado del analisis lexico: ", end="")
    
    if lexicoFlag:
        print("Correcto")
    else:
        print("Error")
    print("==============================================================")
    print("Arbol de la pila: ")
    print("==============================================================")
    while sintactico.getPilaSize() != 0:
            sintactico.pilaTop().printToken(0)
            sintactico.pop_pila()
    

print("Programa terminado, presiona enter para terminar")
input()






