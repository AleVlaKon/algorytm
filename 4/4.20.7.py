def diff_even_odd(a: int, b: int) -> int:
    if a % 2 == 0:
        first_chet = a
        first_nechet = a + 1
    elif a % 2 == 1:
        first_chet = a + 1
        first_nechet = a

    if b % 2 == 0:
        last_chet = b
        last_nechet = b - 1 
    elif b % 2 == 1:
        last_chet = b - 1
        last_nechet = b
    
    n_chet = (last_chet - first_chet) / 2 + 1
    n_nechet = (last_nechet - first_nechet) / 2 + 1

    summ_chet = (first_chet + last_chet) * n_chet / 2
    summ_nechet = (first_nechet + last_nechet) * n_nechet / 2

    return int(summ_chet - summ_nechet)






print(diff_even_odd(3, 11)) #5
