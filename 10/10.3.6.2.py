def merge_sorted_lists(nums1, nums2, nums3):
    i1, i2, i3 = 0, 0, 0
    n1, n2, n3 = len(nums1), len(nums2), len(nums3)
    res = []

    while i1 < n1 or i2 < n2 or i3 < n3:
        min_from_three = min(nums1[i1], nums2[i2], nums3[i3])

        if min_from_three in nums1 and i1 < n1:
            if i1 < n1 - 1:
               i1 += 1 
            elif i1 == n1 - 1:
                nums1[i1] = 10 ** 6 + 1
            res.append(min_from_three)

        elif min_from_three in nums2 and i2 < n2:
            if i2 < n2 - 1:
               i2 += 1 
            elif i2 == n2 - 1:
                nums2[i2] = 10 ** 6 + 1
            res.append(min_from_three)

        elif min_from_three in nums3 and i3 < n3:
            if i3 < n3 - 1:
               i3 += 1 
            elif i3 == n3 - 1:
                nums3[i3] = 10 ** 6 + 1
            res.append(min_from_three)

print(merge_sorted_lists([-3, -2, -1], [4, 7], [0]))