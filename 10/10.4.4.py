def count_pairs_with_greater_difference(nums, k):
    n = len(nums)
    total_pairs = 0
    j = 0
    
    for i in range(n):
        # Увеличиваем j, пока не найдем первый элемент с разностью > k
        # или пока j не выйдет за границы массива
        while j < n and nums[j] - nums[i] <= k:
            j += 1
        
        # Если j не вышел за границы, все элементы от j до конца подходят
        if j < n:
            total_pairs += n - j
        else:
            # Для всех последующих i тоже не будет подходящих j
            break
    
    return total_pairs

nums = [1, 3, 5, 7]
print(count_pairs_with_greater_difference(nums, 0))    # (1, 3), (1, 5), (1, 7), (3, 5), (3, 7), (5, 7)