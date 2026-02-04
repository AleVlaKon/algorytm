from sys import orig_argv


def duplicate_zeros(nums: list[int]) -> None:
    '''
    1. Высчитываем индекс последнего элемента, который будет в списке
    (длина списка - количество нулей)
    2. Идем по списку справа налево от индекса последнего элемента
    3. Если элемент == 0 - вставляем 2 нуля,
       иначе вставляем элемент
    '''
    len_nums = len(nums)
    len_write = len_nums + nums.count(0)

    i = len_nums - 1
    j = len_write - 1
    
    while i >= 0:
        if j < len_nums:
            nums[j] = nums[i]

        if nums[i] == 0:
            j -= 1
            if j <= len_nums:
                nums[j] = 0

        i -= 1
        j -= 1


nums = [3, 0, 2, 7, 0, 1, 4, 5]
duplicate_zeros(nums)
print(nums)