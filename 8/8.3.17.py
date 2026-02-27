from itertools import combinations

def binary_search(nums, k):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle_idx = (left + right) // 2
        center_elem = nums[middle_idx]

        if k == center_elem:
            return middle_idx
        if k > center_elem:
            left = middle_idx + 1
        if k < center_elem:
            right = middle_idx - 1

    return left


def section_sort(nums: list[int]) -> None:
    zeros = [-1]
    zeros_2 = [i for i in range(len(nums)) if nums[i] == 0]
    zeros.extend(zeros_2)
    zeros.append(len(nums) - 1)
    print(zeros)

    for left in range(len(zeros) - 1):
        left_gr = zeros[left]
        right_br = zeros[left + 1]

        for i in range(left_gr, right_br):
            element = nums[i]
            incert_position = binary_search(nums[left_gr:i], element)

            for j in range(i - 1, incert_position - 1, -1):
                nums[j + 1] = nums[j]


            nums[incert_position] = element


def get_sections_indices(lst):
    sections = []
    i = 0
    n = len(lst)
    while i < n:
        # пропускаем нули
        if lst[i] == 0:
            i += 1
            continue
        # нашли начало секции
        start = i
        # идём до конца секции (пока не встретим ноль или конец списка)
        while i < n and lst[i] != 0:
            i += 1
        end = i  # последний элемент секции
        sections.append((start, end))
    return sections


nums = [2, 1, 0, 3, 2, 1, 0]
print(get_sections_indices(nums))
# section_sort(nums)
# print(nums)