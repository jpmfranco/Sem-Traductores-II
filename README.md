# *Nombre: Juan Pablo Mayagoitia Franco Código:217539159*
## Mini analizador lexico

### salida en pantalla del codigo de analizador lexico:
![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/97513ab5-ed50-407e-b097-6c032fde5c26)

## **¿Qué es es un analizador léxico?**
### Un analizador léxico es un módulo destinado a leer caracteres del archivo de  entrada, donde se encuentra la cadena a analizar, reconocer subcadenas que correspondan a símbolos del lenguaje y retornar los tokens correspondientes y sus atributos. 
### Un analizador léxico separa la tarea del analizador sintáctico al encargarse de la identificación y representación de lexemas y componentes léxicos. Este actúa en respuesta a las solicitudes del analizador sintáctico, proporcionándole los componentes ### léxicos necesarios para avanzar en la gramática. Los componentes léxicos, que son los símbolos terminales de la gramática, se obtienen a medida que el analizador sintáctico los requiere. Por lo general, se implementa como una subrutina del analizador ### sintáctico, siendo activado cuando se emite la orden de obtener el siguiente componente léxico. En este proceso, el analizador léxico lee los caracteres de entrada hasta identificar y representar el próximo componente léxico necesario para la gramática.

## **Bibliografia**
### **-** claudiomanzanero. (2017, mayo 15). Unidad 5: Analisis Lexico. Lenguajes y automatas 1 unidades: https://lenguajesyautomatasblog.wordpress.com/2017/05/15/unidad-5-analisis-lexico/
### **-** (S. f.). Edu.ar. Recuperado 21 de enero de 2024, de https://dc.exa.unrc.edu.ar/staff/fbavera/papers/TesisJTLex-Bavera-Nordio-02.pdf

## **Analizador Lexico**

### El analizador lexico va analizando de caracter en caracter y después dependiendo de que tipo es el caracter se va al estado que le corresponde y asi se analiza con todos los caracteres de la cadena y al final se van imprimiendo en pantalla el token el tipo de simbolo y el numero de tipo de simbolo la siguiente imagen es el resultado en consola.


![resultado analizador lexico](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/987ceff2-629c-4d47-93b9-d9c0e3899e42)

## Ejercicios 1 y 2 del analizador sintactico
#### el algoritmo de los ejercicios 1 y 2 es gracias a su gramatica diferente, el del ejercicio 1 utiliza la gramatica ![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/5562cf5a-f1c2-4c1f-9c7e-120a8540d960) y el ejercicio 2 utiliza la gramatica ![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/fa03a4e0-96e6-4345-9155-1ae28959f5ce), además de que las tablas LR son diferentes también por lo que para poder hacer el algoritmo primero debo escribir las dos tablas como son las siguientes: (LR es del ejercicio 1 y LR2 es del ejercicio 2)
![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/98485ac0-319a-4475-8abb-dede3bb57435)

#### utilice el -200 para señalar las casillas que dan error, el 2 y el 3 para el d2 y d3 sucesivamente, utilice el -1 y el -2 para el r1 y r2 sucesivamente y finalmente el -199 para r0

## ejemplo de exitoso en ambos ejercicios:

### Ejercicio 1
  ![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/c736ee27-9f12-400b-8674-35542597b642)


### Ejercicio 2
![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/43324e06-ceeb-4235-a10d-be8239895015)

## ejemplo de los ambos ejercicios no exitosos
### Ejercicio 1
 ![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/275c02c8-1a1c-4f09-8361-4b9e4ef43fc7)


### Ejercicio 2
![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/791b9dc1-3a86-4ed8-ac30-ed59b70c7c91)

## ejemplo del excel entregado anteriormente:

### Ejercicio 1
![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/f6b5dd1d-8c21-43c7-9945-7cfeed13e463)

### Ejercicio 2
![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/81e8c252-e100-42f6-b548-51aa37c80b1f)

## Ejercicios 1 y 2 del analizador sintactico

## Arbol de la pila
### La implimentacion de los objetos en la pila a traves de 3 clases nuevas llamadas Terminal, NoTerminal y Estado que estas tres clases estan heredadas a la clase ElementoPila hacen que se pueda contruir un arbol de la pila para el analizador sintactico.
### Los datos se imprimen normalmente como una tabla pero si la entrada de la cadena es aceptada se imprime a su vez el arbol de la pila 
#### ejemplo de la implementacion del arbol de la pila

![resultado arbol](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/69b05afb-50bd-4740-9ae8-372803881878)

## Sintactico con generacion de codigo (ejemplo)
### int hola;
![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/11e53aa7-c345-4c15-b1bd-37e57987c7cf)

## Etapa final analizador sintactico
### tabla analizador sintactico
![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/86b1d4ed-d1b9-4026-8b78-8d3e70128b77)
![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/421047ee-2c6f-4164-b877-750875dda1a5)
![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/a7ca3bfb-afc1-42a7-9403-5f4178ff0661)

### arbol que genera
![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/93dde53f-d101-4563-8ff9-f08c84782d28)

## Etapa final analizador semantico
### codigo a revisar
![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/b0fe1927-1605-4e61-82ae-87ce4e441259)

### al analizar el codigo anterior nos damos cuenta que x y z estan definidos como int, pero después notamos que las variables ahora valen como flotantes eso es un error entonces se analiza y se notan estos errores de sintaxis
![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/78e44fc2-51d7-4aad-a330-205740a7c4e2)

### ejemplo 1 del classroom analizado
### codigo
![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/fc269198-f9e3-41a6-ad3b-ea7a16567210)

### resultado
![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/4f8514e4-074d-412e-a5a5-08b70c36e6c4)

### ejemplo 2 del classroom analizado
### codigo 
![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/cd2f8206-211d-4b0b-b548-e39d4e9136f4)

### resultado
![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/06011d3e-6e97-4070-b7ba-631d2340864d)

### codigo que compila bien en el semantico
![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/fa23dc38-977f-4823-9354-e636be8e80fd)

## Etapa Final Generacion de codigo

### codigo
![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/2cee1631-5898-484b-9a17-cde937c11f1d)

### codigo generado en ensamblador
![image](https://github.com/jpmfranco/Sem-Traductores-II/assets/103715117/223e1631-579a-4f46-98a6-99a4a202b5f9)


