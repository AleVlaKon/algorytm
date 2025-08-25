def find_index(nums, target):
    right = 1

    while nums[right] < target:
        right *= 2
        
    left = right // 2

    while left <= right:
        middle = (left + right) // 2
        elem = nums[middle]
        if elem == target:
            return middle
        if elem < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


nums1 = [4, 7, 10, 13, 16, ...]
print(find_index(nums1, 13))  

print(find_index(nums1, 11)) 
print(find_index(nums1, 4))