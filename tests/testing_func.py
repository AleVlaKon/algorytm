def subsection_search(nums, start, end):
    for i in range(start + 1, end):
        elem = nums[i]
        j = i - 1
        # пока j указатель меньше начальной позиции
        # и передвигаемый элемент меньше текущего
        while j >= start and elem < nums[j]:
            # перемещаем элементы вперед
            nums[j + 1] = nums[j]
            # а затем уменьшаем счетчик
            j -= 1
        # а потом ставим элемент в нужное место
        nums[j + 1] = elem


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


def section_sort(nums: list[int]) -> None:
    section_list = get_sections_indices(nums)

    for start, end in section_list:
        subsection_search(nums, start, end)