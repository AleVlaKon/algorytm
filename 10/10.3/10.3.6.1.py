def _merge_sorted_lists(nums1, nums2):
    result = []
    i = j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1

    while i < len(nums1):
        result.append(nums1[i])
        i += 1

    while j < len(nums2):
        result.append(nums2[j])
        j += 1

    return result


def merge_sorted_lists(nums1, nums2, nums3):
    res = _merge_sorted_lists(nums1, nums2)
    return _merge_sorted_lists(res, nums3)


print(merge_sorted_lists([1, 4, 6], [2, 4, 7], [2, 3, 5, 6]))
print(merge_sorted_lists([-3, -2, -1], [4, 7], [0]))
