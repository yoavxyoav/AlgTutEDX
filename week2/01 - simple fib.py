def calc_fib(n):

    if n <= 1:
        return n

    fibarray = [1, 1] + [None] * (n-2)

    for i in range(2, n):
        fibarray[i] = fibarray[i-1] + fibarray[i-2]
    return fibarray[n-1]


# n = int(input())
# print(calc_fib(n))
