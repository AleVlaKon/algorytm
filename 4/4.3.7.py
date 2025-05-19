def count_animals(heads: int, legs: int):
    rabbits = (legs - 2 * heads) / 2
    ducks = heads - rabbits
    if int(rabbits) == rabbits and int(ducks) == ducks:
        return int(ducks), int(rabbits)


print(count_animals(2, 6))

print(count_animals(10, 20))
print(count_animals(6, 24))
print(count_animals(1, 1))
print(count_animals(0, 0))
print(count_animals(10, 30))