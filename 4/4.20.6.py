def area_of_tree(n):
    high = 1 + 2 * n
    branches = n ** 2 + n
    return high + branches 

print(area_of_tree(0))
print(area_of_tree(1))
print(area_of_tree(2))
print(area_of_tree(3))
print(area_of_tree(4))