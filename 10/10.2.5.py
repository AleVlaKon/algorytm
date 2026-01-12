from collections import defaultdict

def count_triplets_with_sum(nums1, nums2, nums3, k):
    first_dict = defaultdict(int)
    second_dict = defaultdict(int)

    for a in nums1:
        for b in nums2:
            first_dict[a + b] += 1
    
    for c in nums3:
        second_dict[k - c] += 1

    count = 0
    for k in first_dict:
        count += first_dict[k] * second_dict[k]

    return count


print(count_triplets_with_sum([1, 2], [0, 1], [3, 4], 5))
print(count_triplets_with_sum([1], [1], [1], 3)) 
