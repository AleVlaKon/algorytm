def sequence_type(nums):
    if len(set(nums)) == 1:
        return 'CONSTANT'
    if sorted(nums) == nums:
        if len(set(nums)) == len(nums):
            return 'ASCENDING'
        else:
            return 'WEAKLY ASCENDING'
    if sorted(nums, reverse=True) == nums:
        if len(set(nums)) == len(nums):
            return 'DESCENDING'
        else:
            return 'WEAKLY DESCENDING'
    return 'RANDOM'


def sequence_type(nums):
    variants = {
        'CONSTANT': True,
        'ASCENDING': True,
        'WEAKLY ASCENDING': True,
        'DESCENDING': True,
        'WEAKLY DESCENDING': True,
    }
    
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            variants['ASCENDING'] = False
            variants['DESCENDING'] = False

        if nums[i] > nums[i-1]:
            variants['CONSTANT'] = False
            variants['WEAKLY DESCENDING'] = False
            variants['DESCENDING'] = False

        if nums[i] < nums[i-1]:
            variants['CONSTANT'] = False
            variants['WEAKLY ASCENDING'] = False
            variants['ASCENDING'] = False
    for variant, result in variants.items():
        if result:
            return variant
    
    return 'RANDOM'



print(sequence_type([1, 1, 1, 1, 1]))
print(sequence_type([1, 2, 3, 4, 5]))
print(sequence_type([1, 1, 2, 2, 3]))
print(sequence_type([5, 4, 3, 2, 1]))
print(sequence_type([5, 5, 4, 4, 3]))
print(sequence_type([1, 3, -2, 5, -4]))