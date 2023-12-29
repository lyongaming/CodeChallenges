"""
    ¿ES UN NUMERO PRIMO?
    Escribe un programa que se encargue de comprobar si un numero es o no primo.
    Hecho esto, imprime los numeros primos entre 1 y 100.
"""

def is_prime(num: int) -> bool:
    is_divisible = False
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                is_divisible = True       
                break
        if not is_divisible:
            print(num)

for i in range(1, 101):
    is_prime(i)