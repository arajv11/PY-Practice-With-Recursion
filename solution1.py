def list_nums(n):
    if (n == 0):
        print(0)
    else:
        print(n)
        list_nums(n - 1)

list_nums(5)