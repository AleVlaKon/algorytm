def happy_tickets(n):
    count = 0

    for i1 in range(10):
        for i2 in range(10):
            for i3 in range(10):
                for i4 in range(10):
                    if i1 + i2 + i3 + i4 == n:
                        count += 1
    return count ** 2


print(happy_tickets(1))
print(happy_tickets(2))
print(happy_tickets(3))
print(happy_tickets(15))