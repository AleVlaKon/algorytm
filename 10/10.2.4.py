def pair_with_sum(nums: list[int], k: int):

    result = set()

    for i in nums:
        result.add(k - i)

    for i in nums:
        if i in result and i != k // 2:
            return (i, k - i) if i < k / 2 else (k - i, i)
        

print(pair_with_sum([1, 16, 9, 10, 4], 26))
print(pair_with_sum([4, 5, -1, 10, -5], 0))