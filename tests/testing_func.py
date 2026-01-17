def merge_sorted_lists(nums1, nums2, nums3):
    i1, i2, i3 = 0, 0, 0
    n1, n2, n3 = len(nums1), len(nums2), len(nums3)
    res = []

    while i1 < n1 or i2 < n2 or i3 < n3:
        val1 = val2 = val3 = float('inf')

        if i1 < n1:
            val1 = nums1[i1]

        if i2 < n2:
            val2 = nums2[i2]

        if i3 < n3:
            val3 = nums3[i3]

        if val1 <= val2 and val1 <= val3:
            res.append(val1)
            i1 += 1

        elif val2 <= val3 and val1 <= val1:
            res.append(val2)
            i2 += 1

        else:
            res.append(val3)
            i3 += 1

    return res