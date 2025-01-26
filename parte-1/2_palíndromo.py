def es_palindromo(palabra):
    if not isinstance(palabra, str):
        raise ValueError("El valor ingresado no es una cadena de texto.")
    if palabra == "":
        raise ValueError("La cadena de texto está vacía.")

    palabra = palabra.lower()

    # Se compara el primer carácter con el último, luego el segundo con el penúltimo y así...
    for i in range(0, len(palabra)):
        if palabra[len(palabra) - 1 - i] != palabra[i]:
            return False
    return True


# Ejemplo usando la función
word = input("Ingrese una palabra para verificar si es un palíndromo: ")
if es_palindromo(word):
    print("La palabra es un palíndromo.")
else:
    print("La palabra NO es un palíndromo.")

try:
    es_palindromo("")
except ValueError as exc:
    print(exc)

try:
    es_palindromo(13.45)
except ValueError as exc:
    print(exc)
