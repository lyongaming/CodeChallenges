"""
    LA SUCESION DE FIBONACCI
    Escribe un programa que imprima los 50 primeros numeros de la sucesion 
    de Fibonacci empezando en 0.
    - La serie de Fibonacci se compone por una sucesion de números en 
    la que el siguiente siempre es la suma de los anteriores.
"""

x0, x1 = 0, 1 
for i in range(51):
    if(i == 0 or i == 1):
        print(i)
    else:
        next = x0 + x1
        print(next)
        x0 = x1
        x1 = next