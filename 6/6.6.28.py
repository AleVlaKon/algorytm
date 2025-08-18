def guess(number, result = 10 ** 5):
    if number == result:
        return "Отгадал!"
    elif number > result:
        return "Меньше"
    elif number < result:
        return "Больше"


left = 0
right = 10 ** 10 + 1

while left <= right:
    middle = left + (right - left) // 2
    prom_res = guess(middle)
    if prom_res == "Отгадал!":
        print(middle)
        break
    elif prom_res == "Больше":
        left = middle + 1
    elif prom_res == "Меньше":
        right = middle - 1