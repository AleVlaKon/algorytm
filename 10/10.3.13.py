def min_original_size(nums: str) -> int:
    left = 0
    right = len(nums) - 1

    if len(nums) == 1:
        return 1

    while nums[left] + nums[right] == '01' or nums[left] + nums[right] == '10':
        left += 1
        right -= 1

    start_len = right - left + 1

    return start_len

print(min_original_size('1'))        # 1111001

