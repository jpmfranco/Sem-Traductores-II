import analizerlexic as lexic

class Pila:
    def __init__(self):
        self.lista = []
        
    def push(self, x):
        self.lista.append(x)
        
    def top(self):
        if self.lista:
            return self.lista[-1]
        else:
            raise IndexError("top from empty list")
        
    def pop(self):
        if self.lista:
            return self.lista.pop()
        else:
            raise IndexError("pop from empty list")
        
    def muestra(self):
        for item in reversed(self.lista):
            print(item)
    
    def ejemplo1(self):
        pila.push(2)
        pila.push(3)
        pila.push(4)
        pila.push(5)
        pila.muestra()
        print(pila.top())
        print(pila.top())
        print(pila.pop())
        print(pila.pop())

    def ejemplo2(self):
        cadena = "a"
        lex = lexic.Lexico(cadena)
        while lex.car != '$':
            lex.cambioestado()
            print(lex.simbolo)



pila = Pila()
pila.ejemplo1()
pila.ejemplo2()





