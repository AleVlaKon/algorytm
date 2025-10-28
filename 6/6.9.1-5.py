def f(x):
    return x**7 + 5 * x**2 - 2


epsilon = 0.000001
results = []
for i in range(-2, 1):
    left = i
    right = i + 1
    while right - left > epsilon:
        middle = (right + left) / 2

        if f(middle) * f(right) < 0:
            left = middle

        else:
            right = middle

    results.append(round((left + right) / 2, 6))



print(results)