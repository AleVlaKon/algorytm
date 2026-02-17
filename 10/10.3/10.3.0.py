s = [1, 2, 3, 4, 5, 6, 7]

# print(len(s))

# print(s[4])

left = len(s) - 1
right = len(s) - 1


print(s[left])
print(s[right])

while left >= 0:
    print(left, right)
    left -= 1
    right -=1