def training_time(n, mins, seconds, _break):
    all_time = (n * mins * 60 + n * seconds) + _break * (n - 1)
    return all_time // 60, all_time % 60

