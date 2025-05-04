def max_guests(floors, numbers):
    return (floors - 1) * numbers * 3

print(max_guests(1, 5))
print(max_guests(2, 1))
print(max_guests(10, 10))