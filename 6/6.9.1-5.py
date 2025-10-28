import time


epsilon = 1 / 10 ** 14
left, right = 1, 10 ** 10
start_time = time.time()
while right - left > epsilon:
    middle = (right + left) / 2

    if f(middle) * f(right) < 0:
        left = middle

    else:
        right = middle

end_time = time.time()
print(end_time - start_time)
print((left + right) / 2)

