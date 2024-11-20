def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            return 'Imposible dividir por cero.'
        return a / b
    else:
        return 'Operación inválida'

# Ejemplo usando la función
while True:
    print('------------------------------------')
    operation = input('Introduzca la operación: ')
    a = int(input('Introduzca el primer número: '))
    b = int(input('Introduzca el segundo número: '))
    print(str(calculator(a, b, operation)))
