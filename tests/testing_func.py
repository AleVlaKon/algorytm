def find_peaks(nums):
    count = 0    
    for i in range(1, len(nums)-1):
        if nums[i-1] < nums[i] > nums[i+1]:
            count += 1
    return count 