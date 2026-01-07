from collections import defaultdict


def count_pythagorean_triplets(nums1, nums2, nums3):
    first_dict = defaultdict(int)
    second_dict = defaultdict(int)

    for a in nums1:
        for b in nums2:
            first_dict[a ** 2 + b ** 2] += 1

    
    for c in nums3:
        second_dict[c ** 2] += 1

    
    counter = 0
    for key in first_dict:
        counter += first_dict[key] * second_dict[key]
    
    return counter


print(count_pythagorean_triplets([2, 3, 4], [4, 3], [3, 5]))       # (3, 4, 5), (4, 3, 5)

print(count_pythagorean_triplets([-1, 0, 5], [-2, 1, 3], [4]))
print(count_pythagorean_triplets([-3], [-4], [-5])) 