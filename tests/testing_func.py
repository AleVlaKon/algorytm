def is_flippable_number(num: str):
    left = 0
    right = len(num) - 1

    while left <= right:
        l, r = num[left], num[right]

        if (l, r) == ('6', '9') or (l, r) == ('9', '6') or (l, r) == ('0', '0'):
            left += 1
            right -= 1
        else:
            return False
        
    return True
