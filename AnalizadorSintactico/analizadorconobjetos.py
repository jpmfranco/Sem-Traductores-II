import analizerlexic as lexic

class ElementoPila:
    def __init__(self):
        self.token = ""

    def get_token(self):
        return self.token

    def set_token(self, tokens):
        self.token = tokens

    def print_token(self, nivel):
        print("\t" * nivel + self.token)

class Terminal(ElementoPila):
    def __init__(self, tokens):
        super().__init__()
        self.set_token(tokens)

class NoTerminal(ElementoPila):
    def __init__(self, tokens):
        super().__init__()
        self.set_token(tokens)
        self.nodo = []

    def push_nodo(self, elemento):
        self.nodo.append(elemento)

    def print_token(self, nivel):
        print("\t" * nivel + "E -")
        while len(self.nodo) != 0:
            self.nodo[-1].print_token(nivel + 1)
            self.nodo.pop()

class Estado(ElementoPila):
    def __init__(self, tokens):
        super().__init__()
        self.set_token(tokens)

class Sintactico:
    def __init__(self):
        self.LR = [
            [2, -200, -200, 1],
            [-200, -200, -199, -200],
            [-200, 3, -200, -200],
            [4, -200, -200, -200],
            [-200, -200, -1, -200]
        ]
        self.LR2 = [
            [2, -200, -200, 1],
            [-200, -200, -199, -200],
            [-201, 3, -2, -200],
            [2, -200, -200, 4],
            [-200, -200, -1, -200]
        ]
        self.pila = []
        self.pila.append(Terminal("$"))
        self.pila.append(Estado("0"))

    def empezar(self):
        self.pila.append(Terminal("$"))
        self.pila.append(Estado("0"))

    def get_LR_at(self, fila, columna):
        return self.LR2[fila][columna]

    def print_LR(self):
        for i in range(5):
            for j in range(4):
                print(self.get_LR_at(i, j), end="\t")
            print()

    def pop_pila(self):
        self.pila.pop()

    def pila_top(self):
        return self.pila[-1]

    def salida(self, tokens, tipo):
        if tipo < 0 or tipo > 3:
            return -200
        fila = int(self.pila_top().get_token())
        if fila < 0 or fila > 4:
            return -200
        estado = self.get_LR_at(fila, tipo)
        if estado == -199:
            return estado
        elif estado >= 0:
            self.pila.append(Terminal(tokens))
            self.pila.append(Estado(str(estado)))
            return estado
        elif estado == -1:
            return self.regla1()
        elif estado == -2:
            return self.regla2()
        else:
            return -200

    def regla1(self):
        nt = NoTerminal("E")
        for i in range(6):
            nt.push_nodo(self.pila_top())
            self.pop_pila()
        fila = int(self.pila_top().get_token())
        estado = self.get_LR_at(fila, 3)
        if estado < -199:
            return -200
        else:
            self.pila.append(nt)
            self.pila.append(Estado(str(estado)))
            return -1

    def regla2(self):
        nt = NoTerminal("E")
        for i in range(2):
            nt.push_nodo(self.pila_top())
            self.pop_pila()
        fila = int(self.pila_top().get_token())
        estado = self.get_LR_at(fila, 3)
        if estado < -199:
            return -200
        else:
            self.pila.append(nt)
            self.pila.append(Estado(str(estado)))
            return -2

    def get_pila_size(self):
        return len(self.pila)

# Assuming Lexico and Sintactico are classes that have been defined in Python
# with equivalent functionality to their C++ counterparts.



cadena = "a+b+c+d+e+f"
lexico = lexic.Lexico(cadena)
sintactico = Sintactico()
lexico.entrada(cadena)
print("Estado en pila\t||\tEntrada\t\t||\tSalida")
print("======================================================")
lexicoFlag = True
entradaSint = lexico.getCadenaFromInd()
back = sintactico.pila_top().get_token()
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
    back = sintactico.pila_top().get_token()
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
    while sintactico.get_pila_size() != 0:
            sintactico.pila_top().print_token(0)
            sintactico.pop_pila()
    

print("Programa terminado, presiona enter para terminar")
input()






