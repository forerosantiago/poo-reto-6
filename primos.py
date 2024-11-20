def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def filtrar_primos(lista):
    return [numero for numero in lista if es_primo(numero)]


# Ejemplo de uso
numeros = [1, 2,3, 4, 5, 6, 7, 8, 9, 10]
print(filtrar_primos(numeros))