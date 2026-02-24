from collections import defaultdict

def uniques_count_in_every_sublist(nums, k):
    left = 0
    right = k
    n = len(nums)
    diapazon = defaultdict(int) 

    for i in range(k):
        diapazon[nums[i]] += 1

    res = [len(diapazon)]

    while right < n:
        left_elem = nums[left]
        diapazon[left_elem] -= 1
        if diapazon[left_elem] == 0:
            del diapazon[left_elem]

        right_elem = nums[right]
        diapazon[right_elem] += 1
        res.append(len(diapazon))
        
        left += 1
        right += 1

    return res