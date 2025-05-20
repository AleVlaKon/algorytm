def count_days(cur: int) -> int:
    days = 0
    while cur % 2 != 0:
        days += 1
        cur = (cur - 1) / 2
    return days

print(count_days(5905580031))