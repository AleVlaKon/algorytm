def snake(n):
    for i in range(n):
        if i % 4 in (0, 2):
            print('*' * n)
        elif i % 4 == 1:
            print('*'.rjust(n, " "))
        elif i % 4 == 3:
            print('*')


snake(5)