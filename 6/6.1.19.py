def elements_in_the_range(nums: list[int], start: int, end: int):
    set_one = set(nums)
    set_two = set(range(start, end + 1))

    return set_two.issubset(set_one)


print(elements_in_the_range([1, 5, 6, 2, 3, 8, 9, 4], 1, 5))
print(elements_in_the_range([1, 3, 5, 2, 7, 8, 4], 2, 6))