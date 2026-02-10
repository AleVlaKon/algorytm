def count_pairs_with_greater_difference(nums: list[int], k: int) -> int:
    left1 = 0
    left2 = 0

    while left2 < len(nums) - 1 and nums[left2] - nums[left1] < k:
        left2 += 1
        

    while left1 < len(nums) - 1 and nums[left2] - nums[left1] > k:
        left1 += 1

    pairs = (left1 + 1) * (len(nums) - left2) - 1
    return pairs



nums = [1, 3, 5, 7]
print(count_pairs_with_greater_difference(nums, 0))    # (1, 3), (1, 5), (1, 7), (3, 5), (3, 7), (5, 7)