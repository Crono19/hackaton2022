def main():
    number = int(input('Por favor ingrese el numero al que le desea sacar el factorial: '))
    print(f'El factorial del numero {number}! es: {factorial(number)}')


def factorial(number):
    result = 0
    if number == 0 or number == 1:
        result = 1
    elif number > 1:
        result = number * factorial(number - 1)

    return result


main()
