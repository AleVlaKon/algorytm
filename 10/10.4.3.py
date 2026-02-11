def min_difference(nums1, nums2):
    nums1.sort()
    nums2.sort()


    left1, left2 = 0, 0
    min_diff = float('inf')

    while left1 < len(nums1) and left2 < len(nums2):
        if abs(nums1[left1] - nums2[left2]) < min_diff:
            min_diff = abs(nums1[left1] - nums2[left2])
        if nums1[left1] < nums2[left2]:
            left1 += 1
        else:
            left2 += 1

    return min_diff




print(min_difference([6, 4, 5], [3, 1, 5, 8]))      # (5, 5)