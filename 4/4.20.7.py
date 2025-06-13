def diff_even_odd(a: int, b: int) -> int:
    first_chet = a + a % 2
    first_nechet = a - a % 2 + 1

    last_chet = b - b % 2
    last_nechet = b + b % 2 - 1 
    
    n_chet = (last_chet - first_chet) // 2 + 1
    n_nechet = (last_nechet - first_nechet) // 2 + 1

    summ_chet = (first_chet + last_chet) * n_chet // 2
    summ_nechet = (first_nechet + last_nechet) * n_nechet // 2

    return summ_chet - summ_nechet






print(diff_even_odd(3, 11)) #5
