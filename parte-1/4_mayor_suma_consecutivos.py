# Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.


def mayor_suma_consecutivos(lista):

    if not isinstance(lista, list):
        raise ValueError("El valor ingresado no es una lista.")
    if not all(isinstance(n, int) for n in lista):
        raise ValueError("La lista debe contener solo números enteros.")

    suma_mayor = lista[0] + lista[1]

    for i in range(1, len(lista) - 1):
        suma_actual = lista[i] + lista[i + 1]
        if suma_actual > suma_mayor:
            suma_mayor = suma_actual

    return suma_mayor


# Ejemplo de uso
print(mayor_suma_consecutivos([1, 2, 3, 5, 10, 6, 11]))

try:
    print(mayor_suma_consecutivos([1, 2, 3, 4, 5, 6, 7, 8, 9, "10"]))
except ValueError as exc:
    print(exc)
