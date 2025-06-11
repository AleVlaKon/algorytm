def get_exam_position(n: int, k: int) -> int:
    if k % 2 != 0:
        return k // 2 + 1
    else:
        if n % 2 == 0:
            return n // 2 + k // 2
        else:
            return n // 2 + k // 2 + 1

# print(get_exam_position(10, 1))  #1
# print(get_exam_position(10, 3))  #2
# print(get_exam_position(10, 5))  #3
# print(get_exam_position(10, 7))  #4
print(get_exam_position(10, 2))  #6
print(get_exam_position(10, 4))  #7
print(get_exam_position(10, 6))  #8
print(get_exam_position(10, 8))  #9
print(get_exam_position(10, 10)) #10
print(get_exam_position(1, 1))   #1
print(get_exam_position(11, 2))
print(get_exam_position(3, 2))