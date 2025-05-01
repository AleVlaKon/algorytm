import math

def iterated_log(n: int) -> int:
    iteration_count = 0
    while n > 1:
        n = math.log2(n)
        iteration_count += 1
    return iteration_count
    



print(iterated_log(1))     # 1
print(iterated_log(2))     # log2(2) = 1
print(iterated_log(3))     # log2(3) = 1.58; log2(1.58) = 0.66
print(iterated_log(4))     # log2(4) = 2; log2(2) = 1
print(iterated_log(5))     # log2(5) = 2.32; log2(2.32) = 1.21; log2(1.21) = 0.27
print(iterated_log(10))    # log2(10) = 3.32; log2(3.32) = 1.73; log2(1.73) = 0.79


