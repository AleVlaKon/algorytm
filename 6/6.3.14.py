from collections import Counter

def find_number(nums):
    count_dict = Counter(nums)
    max_key = -1
    for key, value in count_dict.items():
        if key == value and key > max_key:
            max_key = key
    return max_key


data = [3, 3, 3]
print(find_number(data))