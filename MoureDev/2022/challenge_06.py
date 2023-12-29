"""
    INVIRTIENDO CADENAS
    Crea un programa que invierta el orden de una cadena de texto 
    sin usar funciones propias del lenguaje que lo hagan de forma automática.
    - Si le pasamos "Hola mundo" nos retornaria "odnum aloH" 
"""

def reverse(text : str) -> str:
    return text[::-1]

print(reverse("Hola mundo"))