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


def problem3():
    number = 600851475143
    largest_prime_factor = 0
    i = 2

    while number != 1:
        if number % i == 0:
            number = number / i
            prime_factor = i
            if prime_factor > largest_prime_factor:
                largest_prime_factor = prime_factor
        i += 1

    print(largest_prime_factor)


def problem5():
    # Smallest multiple

    number = 0
    i = 20
    dividers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    while number == 0:
        z = 0
        for n in dividers:
            if i % n == 0:
                z += 1
        if z == 10:
            number = i
        i += 1

    print(number)


def problem6():
    # Sum square difference

    sum_of_squares = 0
    sum = 0

    for i in range(101):
        sum_of_squares += i*i
        sum += i

    squares_of_sum = sum*sum

    print(squares_of_sum-sum_of_squares)
