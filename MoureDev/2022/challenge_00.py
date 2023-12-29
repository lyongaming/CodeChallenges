"""
    EL FAMOSO "FIZZ BUZZ":
    Escribe un programa que muestre por consola (con un print) los
    numeros del 1 al 100 (ambos incluidos y con un salto de linea entre
    cada impresion), sustituyendo los siguientes:
    - Multiplos de 3 por la palabra "fizz".
    - Multiplos de 5 por la palabra "buzz".
    - Multiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"  
"""

for i in range(1, 101):
    out = ""
    if i % 3 == 0:
        out += "fizz"
    if i % 5 == 0:
        out += "buzz"
    print(f"{out or i}")  