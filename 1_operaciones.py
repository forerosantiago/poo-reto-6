def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        try:
            return a / b
        except ZeroDivisionError as exc:
            raise ZeroDivisionError('No se puede dividir por cero') from exc
    else:
        raise TypeError('Operación no válida')


# Ejemplo usando la función
while True:
    print('------------------------------------')
    op = input('Introduzca la operación: ')

    try:
        first = int(input('Introduzca el primer número: '))
        second = int(input('Introduzca el segundo número: '))
    except ValueError:
        print('Los números deben ser números enteros.')
        continue
    print(str(calculator(first, second, op)))
