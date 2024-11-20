# Soluciones reto 1 - POO 2024-2 

## 1. Calculadora con operaciones
Se creó una función que tiene tres argumentos de entrada. Los primeros dos argumentos son dos números reales y el tercer argumento es un string con una de las siguientes opciones: `+, -, * ó /`, que corresponden a la operación de suma, resta, multiplicación y división respectivamente. Además de esto, la función cuenta con un fallback en caso de que el tercer sea algo diferente a las opciones posibles.

Adicionalmente, se muestra un ejemplo de cómo usar la función en un bucle infinito `while` que acepta inputs del usuario de forma interactiva.

### 2. Detector de palíndromos
La función recibe un argumento del typo `string`, luego compara el primer carácter con el último, luego el segundo con el penúltimo y así, en caso de que todas las parejas de carácteres coincidan, la palabra es un palíndromo.

### 3. Filtro de números primos
En este reto se implementaron dos funciones, una para verificar que un número dado sea primo y otra para quitar de una lista los números que no sean primos.
**Nota:** Se utiliza el syntax de `list comprehension` para crear una nueva lista basada en valores de una lista existente de forma más compacta.

### 4. Mayor suma entre dos elementos consecutivos de una lista
Se escribió una función que recibe como argumento una lista de números enteros y retorna la mayor suma de dos elementos consecutivos (en la lista, no númericamente), iterando cada elemento de la lista y comparándolo con el siguiente elemento de la misma lista.

### 5. Detector de palabras con los mismos carácteres
Se creó una función que recibe una lista de elementos tipo `string`, los carácteres de cada elemento se ordenan alfabéticamente y se almacenan como la llave de un grupo en un diccionario, por último se agrega cada palabra a la llave del diccionario. Por último se itera sobre los grupos del diccionario y se retorna una lista con las palabras cuyos grupos tienen dos o más elementos.