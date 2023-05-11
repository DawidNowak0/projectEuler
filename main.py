def problem1():
    # Multiples of 3 or 5

    sum = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print(sum)


def problem2():
    # Even Fibonacci numbers

    sum = 0
    first = 0
    second = 1
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


def problem6():
    # Sum square difference

    sumOfSquares = 0
    sum = 0

    for i in range(101):
        sumOfSquares += i*i
        sum += i

    squaresOfSum = sum*sum

    print(squaresOfSum-sumOfSquares)
