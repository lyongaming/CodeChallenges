"""
    ¿ES UN ANAGRAMA?
    Escribe una función que reciba dos palabras (String) y retorne 
    verdadero o falso (Bool) según sean o no anagramas.
    - Un Anagrama consiste en formar una palabra reordenando TODAS 
    las letras de otra palabra inicial.
    - NO hace falta comprobar que ambas palabras existan.
    - Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(w1: str, w2: str) -> bool:
    if w1.lower() == w2.lower():
        return False
    return sorted(w1.lower()) == sorted(w2.lower())

print(is_anagram("Hola", "Hola"))
print(is_anagram("Anal", "Lana"))