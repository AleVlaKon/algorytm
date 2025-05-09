def hamming_distance(s1, s2):
    distance = 0
    for i, k in zip(s1, s2):
        if i != k:
            distance += 1
    return distance

