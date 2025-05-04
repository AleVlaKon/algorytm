def intersections(a, b, c, k, m):
    result = set()
    k_a = a
    k_b = b - k
    k_c = c - m
    discriminant = k_b ** 2 - 4 * k_a * k_c
    if discriminant >= 0:    
        x1 = (-k_b + discriminant ** 0.5)/(2 * k_a)
        x2 = (-k_b - discriminant ** 0.5)/(2 * k_a)
        y1 = k * x1 + m
        y2 = k * x2 + m
        result = {(x1, y1), (x2, y2)}
    return result        


print(intersections(1, 0, 0, 1, 0))