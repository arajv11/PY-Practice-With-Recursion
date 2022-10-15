def natural_nums(n):
    if (n == 1):
        print(1)
    else: 
        print(n)
        natural_nums(n - 1)

natural_nums(5)