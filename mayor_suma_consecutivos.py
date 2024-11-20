# Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

def mayor_suma_consecutivos(lista):
    suma_mayor = lista[0] + lista[1]

    for i in range(1, len(lista) - 1):
        suma_actual = lista[i] + lista[i + 1]
        if suma_actual > suma_mayor:
            suma_mayor = suma_actual
    
    return suma_mayor

# Ejemplo de uso
print(mayor_suma_consecutivos([1,2, 3, 5, 10, 6, 11 ]))