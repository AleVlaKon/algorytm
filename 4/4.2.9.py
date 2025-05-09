def even_odd(nums: list[int]):
    first_num = nums[0] % 2
    for number in nums:
        if not number % 2 == first_num:
            return False
    return True 
