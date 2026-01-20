from itertools import cycle

def card_game_results(nums: list[int]):
    left = 0
    right = len(nums) - 1

    res = {'Timur': 0, "Artur": 0}
    choise = cycle(["Timur", "Artur"])

    while left <= right:
        if nums[left] > nums[right]:
            res[next(choise)] += nums[left]
            left += 1
        else:
            res[next(choise)] += nums[right]
            right -= 1

    return res["Timur"], res["Artur"]

print(card_game_results([6, 2, 1, 5, 3, 4]))
print(card_game_results([3, 5, 1, 4, 2]))
print(card_game_results([1]))
print(card_game_results([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
