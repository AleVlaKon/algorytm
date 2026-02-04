def duplicate_zeros(nums: list[int]) -> None:
    '''
    1. Высчитываем индекс последнего элемента, который будет в списке
    (длина списка - количество нулей)
    2. Идем по списку справа налево от индекса последнего элемента
    3. Если элемент == 0 - вставляем 2 нуля,
       иначе вставляем элемент
    '''
    count = 0

    for i in nums:
        if i == 0:
            count += 1
    print(count)

    # if nums[-1] == 0:
    #     count -= 1

    if nums[-2] == 0:
        count -= 1

    count = len(nums) - count

    read = count - 1
    write = len(nums) - 1

    while read >= 0:
        nums_read = nums[read]
        nums_write = nums[write]
        if nums[read] == 0:
            if write < len(nums):
                nums[write] = 0
                write -= 1
            if write < len(nums):
                nums[write] = 0
                write -= 1
        else:
            if write < len(nums):
                nums[write] = nums[read]
            write -= 1

        read -= 1



nums = [3, 0, 2, 7, 0, 1, 4, 5]
duplicate_zeros(nums)
print(nums)