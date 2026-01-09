from collections import defaultdict


def count_valid_quadruplets(nums1, nums2, nums3, nums4):
    first_dict = defaultdict(int)
    second_dict = defaultdict(int)

    func1 = lambda a, b: (a + b) ** 2
    func2 = lambda c, d: (d - c) ** 2


    for a in nums1:
        for b in nums2:
            first_dict[func1(a, b)] += 1

    for c in nums3:
        for d in nums4:
            if d == 0:
                second_dict[-c] += 1
            else:
                second_dict[func2(c, d)] += 1

    counter = 0
    for ket in first_dict:
        counter += first_dict[ket] * second_dict[ket]
    
    return counter


print(count_valid_quadruplets([1, 2], [3, 4], [3, 6], [7, 8]))
print(count_valid_quadruplets([2, -1, 3], [-1, 0, 1], [4, 2, 5], [-2, 0]))
print(count_valid_quadruplets([1, 1, 3], [1, 1], [2, 7], [0, 0]))
print(count_valid_quadruplets([1], [2], [3], [4]))
print(count_valid_quadruplets([1, 1, 3], [1, 1], [2, 7], [0, 0]))
print(count_valid_quadruplets([0, 0], [0, 0], [0, 0], [0, 0]))



