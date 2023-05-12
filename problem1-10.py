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


def problem7():
    # 10001st prime

    prime = []
    n = 2

    while len(prime) < 10001:
        is_prime = 1
        for i in prime:
            if n % i == 0:
                is_prime = 0
        if is_prime == 1:
            prime.append(n)
        n += 1

    print(prime[len(prime)-1])


def problem8():
    # Largest product in a series

    digits = ['7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450']
    numbers = []
    largest_product = 0

    for _ in digits:
        for i in _:
            if len(numbers) != 13:
                numbers.append(i)
            else:
                numbers.pop(0)
                numbers.append(i)
                product = 1
                for number in numbers:
                    product = product * int(number)
                if product > largest_product:
                    largest_product = product

    print(largest_product)


def problem10():
    # Summation of primes

    sum = 0
    n = 2
    prime = []

    while n < 2000000:
        is_prime = 1
        for i in prime:
            if i > int(n/2)+1:
                break
            if n % i == 0:
                is_prime = 0
        if is_prime == 1:
            prime.append(n)
            print(n)
        n += 1
    for i in prime:
        sum += i
    print(sum)

   