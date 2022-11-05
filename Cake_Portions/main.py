def main():
    friends = int(input('Por favor ingrese la cantidad de amigos que tiene: '))
    portions = int(input('Por favor ingrese la cantidad de porciones que desean sus amigos: '))
    print(cake_slices(friends, portions))


def cake_slices(friends, portions):
    total_portions = friends * portions
    total_cakes = total_portions / 4

    return f'Se necesita un total de {total_cakes} pasteles para satisfacer la cantidad de porciones requeridas'


main()
