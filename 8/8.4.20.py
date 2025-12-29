from collections import Counter

def count_pairs(nums):
    data = Counter(nums)


    total_pairs = 0
    for count in data.values():
        total_pairs += count * (count + 1) // 2

    return total_pairs


print(count_pairs([1, 2, 3, 4]))   
print(count_pairs([2, 4, 2])) 
print(count_pairs([4, 4]))  
print(count_pairs([1]))       
print(count_pairs([-1, -2, -1, -2])) 
print(count_pairs([1, 1, 1])) 