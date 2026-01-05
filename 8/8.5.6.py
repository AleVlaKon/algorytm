def key_sort(num):
    if num == 0:
        return (1, 0)
    
    count_drills = 0
    abs_num = abs(num)
    
    while abs_num > 0:
        last = abs_num % 10
        if last in (0, 6, 9):
            count_drills += 1
        elif last == 8:
            count_drills += 2
        abs_num //= 10
    
    return count_drills, num


def holey_sort(nums):
    nums.sort(key=key_sort)


nums = [-8, 0, -9, -6]
holey_sort(nums)
print(nums)