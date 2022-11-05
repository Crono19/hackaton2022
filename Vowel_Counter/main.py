def main():
    string = str(input('Por favor ingrese su cadena de texto: '))
    print(vowelCounter(string))


def vowelCounter(string):
    counter = 0
    string2 = ''
    for character in string:
        if character.upper() in "AEIOU":
            counter += 1
            string2 += character

    return f'Hay un total de {counter} vocales. ' \
           f'Las vocales son: {string2}'



main()
