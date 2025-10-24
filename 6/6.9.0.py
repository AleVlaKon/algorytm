def f(x):
    return x**5 + 5 * x**3 + 3 * x - 4

left, right = 0, 1
epsilon = 0.000001

while right - left > epsilon:
        middle = (right + left) / 2

        if f(middle) < 0:
            left = middle

        else:
            right = middle

print(left, right)