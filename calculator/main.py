def add(numbers):
    result = 0
    for number in numbers:
        result += number

    return result


def subtract(numbers):
    result = numbers[0]
    for number in numbers[1: len(numbers)]:
        result -= number

    return result


def operation(numbers, base, option):
    result = ''
    for i in range(len(numbers)):
        if base == '1':
            result += bin(numbers[i])[2:]
        elif base == '2':
            result += str(numbers[i])
        elif base == '3':
            result += hex(numbers[i])[2:]

        if i + 1 != len(numbers):
            if option == '2':
                result += ' + '
            elif option == '3':
                result += ' - '

    return result


def main():
    numbers = []

    while True:
        print('Select a base')

        print('1 - Binary')
        print('2 - Decimal')
        print('3 - Hexadecimal')
        base = input('Insert the base: ')
        print('')
        if base == '1' or base == '2' or base == '3':
            break
        else:
            print('Select a correct option')
            print('')

    while True:
        print('Select an operation')

        print('1 - Insert number')
        print('2 - Add numbers')
        print('3 - Subtract numbers')
        print('4 - Exit')
        option = input('Insert the option: ')
        print('')

        if option == '1':
            number = input('Insert the number: ')

            if base == '1':
                numbers.append(int(number, 2))
            elif base == '2':
                numbers.append(int(number))
            elif base == '3':
                numbers.append(int(number, 16))

        elif option == '2':

            print(operation(numbers, base, option))

            print(f'Result in binary: {bin(add(numbers))[2:]}')
            print(f'Result in decimal: {add(numbers)}')
            print(f'Result in hexadecimal: {hex(add(numbers))[2:]}')

        elif option == '3':

            print(operation(numbers, base, option))

            if subtract(numbers) < 0:
                print(f'Result in binary: -{bin(subtract(numbers))[3:]}')
                print(f'Result in decimal: {subtract(numbers)}')
                print(f'Result in hexadecimal: -{hex(subtract(numbers))[3:]}')

            else:
                print(f'Result in binary: {bin(subtract(numbers))[3:]}')
                print(f'Result in decimal: {subtract(numbers)}')
                print(f'Result in hexadecimal: {hex(subtract(numbers))[3:]}')

        elif option == '4':
            print('Good bye')
            break

        else:
            print('Select a correct option')

        print('')


main()
