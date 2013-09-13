def iterative_fib(n):
    # 0, 1, 1, 2, 3, 5, 8, 13
    a = 0
    b = 1
    total = 0
    for i in xrange(n):
        total = a + b
        b, a = a, total
    return total

if __name__ == "__main__":
    n = 7
    print iterative_fib(n)
