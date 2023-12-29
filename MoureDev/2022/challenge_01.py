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
    w1_lowcase = w1.lower()
    w2_lowcase = w2.lower()
    if w1_lowcase == w2_lowcase:
        return False
    letters_w1 = count_letters(w1_lowcase)
    letters_w2 = count_letters(w2_lowcase)
    return letters_w1 == letters_w2

def count_letters(word : str) -> dict[str, int]:
    letters = dict.fromkeys(word, 0)
    for letter in letters.keys():
        letters[letter] = word.count(letter)
    return letters

print(is_anagram("Hola", "Hola"))
print(is_anagram("Anal", "Lana"))