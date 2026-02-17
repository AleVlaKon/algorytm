
def have_common_element(nums1, nums2):
    left1 = 0
    left2 = 0

    while left1 < len(nums1) and left2 < len(nums2):
        if nums1[left1] == nums2[left2]:
            return True
        elif nums1[left1] < nums2[left2]:
            left1 += 1
        else:
            left2 += 1        

    return False


print(have_common_element([1, 2, 3, 4], [2, 8, 16]))
print(have_common_element([1, 2, 3], [1, 2, 3, 4]))
print(have_common_element([1, 3], [0, 2, 4, 8]))
print(have_common_element([1], [2]))