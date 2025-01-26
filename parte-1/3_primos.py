def es_primo(numero):

    if not isinstance(numero, int):
        raise ValueError("El valor ingresado no es un número entero.")

    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def filtrar_primos(lista):
    if not isinstance(lista, list):
        raise ValueError("El valor ingresado no es una lista.")
    return [numero for numero in lista if es_primo(numero)]


# Ejemplo de uso
numeros = [1, 2,3, 4, 5, 6, 7, 8, 9, 10]
print(filtrar_primos(numeros))

try:
    es_primo(1.4)
    print(es_primo(5))
    print(es_primo([5]))
    print(es_primo(1.4))

except ValueError as exc:
    print(exc)

print(filtrar_primos((1,2,3,4,5)))
