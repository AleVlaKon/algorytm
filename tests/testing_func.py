from collections import defaultdict

def happy_tickets(n):
    first_dict = defaultdict(int)
    second_dict = defaultdict(int)

    for a in range(10):
        for b in range(10):
            first_dict[a + b] += 1

    for c in range(10):
        for d in range(10):
            second_dict[n - c - d] += 1
    
    counter = 0
    for ket in first_dict:
        counter += first_dict[ket] * second_dict[ket]
    
    return counter ** 2