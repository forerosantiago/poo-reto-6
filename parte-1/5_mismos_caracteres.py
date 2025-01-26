def mismos_caracteres(lista):

    if not isinstance(lista, list):
        raise ValueError("El valor ingresado no es una lista.")
    # Se crea un diccionario para las palabras con los mismos caracteres
    grupos = {}

    for palabra in lista:
        # Se ordenan alfabeticamente los caracteres de cada palabra para generar una clave única para cada grupo
        
        clave = "".join(sorted(palabra))
        # Se verifica si ya existe un grupio con la misma clave
        if clave in grupos:
            grupos[clave].append(palabra)
        else:
            grupos[clave] = [palabra]

    # Se filtran y se retornan los grupos que tengan más de un elemento
    resultado = []
    for palabras in grupos.values():
        if len(palabras) > 1:
            resultado.extend(palabras)
    
    return resultado

# Ejemplo de uso
entrada = ["amor", "roma", "perro", "sapo", "paso", "sapa"]

print(mismos_caracteres(entrada))

try:
    mismos_caracteres("amor")
except ValueError as exc:
    print(exc)