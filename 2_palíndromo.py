def es_palindromo(palabra):
    palabra = palabra.lower()

    # Se compara el primer carácter con el último, luego el segundo con el penúltimo y así...
    for i in range(0, len(palabra)):
        if palabra[len(palabra) -1 -i] != palabra[i]:
            return False
    return True

# Ejemplo usando la función
palabra = input("Ingrese una palabra para verificar si es un palíndromo: ")
if es_palindromo(palabra):
    print("La palabra es un palíndromo.")
else:
    print("La palabra NO es un palíndromo.")
