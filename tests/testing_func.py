def check_animals(animal):
    return int(animal) == animal and animal >= 0


def count_animals(heads: int, legs: int):
    rabbits = (legs - 2 * heads) / 2
    ducks = heads - rabbits
    if check_animals(rabbits) and check_animals(ducks):
        return int(ducks), int(rabbits)