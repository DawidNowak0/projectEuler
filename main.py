def problem1():
    sum = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print(sum)


def problem2():
    sum = 0
    first = 0
    second = 1
    fib = 0
    i = 0
    while i < 1:
        fib = first + second
        first = second
        second = fib
        if fib > 4000000:
            break
        if fib % 2 == 0:
            sum += fib
    print(sum)


problem2()
