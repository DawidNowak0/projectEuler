import math


def problem1():
    # Multiples of 3 or 5
    # 233168

    sum = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    print(sum)


def problem2():
    # Even Fibonacci numbers
    # 4613732

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
    # Largest prime factor
    # 6857

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


def problem4():
    # Largest palindrome product
    #  906609

    a = 100
    b = 100
    largest_palindrome = 0

    while b != 1000:
        product = [a * b]
        reverse = []

        for _ in product:
            for i in str(_):
                reverse.insert(0, i)

        reverse = "".join(reverse)
        product = product[0]

        if str(product) == str(reverse):
            if product > largest_palindrome:
                largest_palindrome = product
        if a < 1000:
            a += 1
        else:
            b += 1
            a = b

    print(largest_palindrome)


def problem5():
    # Smallest multiple
    # 232792560

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
    # 25164150

    sum_of_squares = 0
    sum = 0

    for i in range(101):
        sum_of_squares += i * i
        sum += i

    squares_of_sum = sum * sum

    print(squares_of_sum - sum_of_squares)


def problem7():
    # 10001st prime
    # 104743

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

    print(prime[len(prime) - 1])


def problem8():
    # Largest product in a series
    # 23514624000

    digits = ['73167176531330624919225119674426574742355349194934'
              '96983520312774506326239578318016984801869478851843'
              '85861560789112949495459501737958331952853208805511'
              '12540698747158523863050715693290963295227443043557'
              '66896648950445244523161731856403098711121722383113'
              '62229893423380308135336276614282806444486645238749'
              '30358907296290491560440772390713810515859307960866'
              '70172427121883998797908792274921901699720888093776'
              '65727333001053367881220235421809751254540594752243'
              '52584907711670556013604839586446706324415722155397'
              '53697817977846174064955149290862569321978468622482'
              '83972241375657056057490261407972968652414535100474'
              '82166370484403199890008895243450658541227588666881'
              '16427171479924442928230863465674813919123162824586'
              '17866458359124566529476545682848912883142607690042'
              '24219022671055626321111109370544217506941658960408'
              '07198403850962455444362981230987879927244284909188'
              '84580156166097919133875499200524063689912560717606'
              '05886116467109405077541002256983155200055935729725'
              '71636269561882670428252483600823257530420752963450']
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


def problem9():
    # Special Pythagorean triplet
    # 31875000

    a = 1
    b = 2
    c = 0
    sum = 0

    while sum != 1000:
        if b < 500:
            b += 1
        else:
            a += 1
            b = a + 1
        c = (a * a) + (b * b)
        c = math.sqrt(c)
        if int(c) == c:
            sum = a + b + c

    print(int(a * b * c))


def problem10():
    # Summation of primes
    # 142913828922

    sum = 0
    n = 2
    prime = []

    while n < 2000000:
        is_prime = 1
        for i in prime:
            if i > int(n / 2) + 1:
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


def problem17():
    # Number letter counts
    #

    count = ""
    one_nine = ['', "one", 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    ten_nineteen = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    twenty_ninety = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    for i in range(1, 1001, 1):
        if i < 10:
            count += one_nine[i]
        elif i < 20:
            count += ten_nineteen[i-10]
        elif i < 100:
            for j in range(8):
                for n in range(0, 10, 1):
                    count += twenty_ninety[j]
                    count += one_nine[n]
        elif i < 1000:
            for x in range(9):
                for j in range(8):
                    for n in range(0, 10, 1):
                        count += one_nine[n]
                        count += twenty_ninety[j]
                        count += "hundred"
                        count += one_nine[x]
        else:
            count += "onethousand"

    print(len(count))


problem17()
