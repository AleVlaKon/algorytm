def min_difference(nums1, nums2):
    nums1.sort()
    nums2.sort()

    left = 0
    right = len(nums2) - 1
    min_diff = float('inf')
    min1 = 0
    min2 = 0

    while left < len(nums1) and right > 0:
        if nums1[left] > nums2[right]:
            left += 1
        else:
            right -= 1




print(min_difference([4, 1, 5], [8, 11, 9, 10]))    # (5, 8) 