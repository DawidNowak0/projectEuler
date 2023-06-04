def problem21():
    # Amicable Numbers
    # 31626

    def proper_divisors(num):
        sum = 0
        divisors = []
        for i in range(1, int(num/2+1)):
            if num % i == 0:
                divisors.append(i)
        for number in divisors:
            sum += int(number)
        return sum

    sum_of_amicable = 0

    for a in range(1, 10000):
        b = proper_divisors(a)
        if a != b:
            if proper_divisors(b) == a:
                sum_of_amicable += a
    print(sum_of_amicable)


def problem22():
    # Names Scores
    # 871198282

    file = open("names.txt", "r")
    names = []
    name = ""

    for line in file:
        for letter in line:
            if letter == '"' and len(name) > 0:
                names.append(name)
                name = ""
            elif letter == '"' or letter == ",":
                a = 0
            else:
                name += letter
    names.sort()
    index = 1
    total = 0

    for name in names:
        score = 0
        for letter in name:
            score += ord(letter)-64
        score *= index
        total += score
        index += 1
    print(total)


def problem25():
    # 1000-digit Fibonacci Number
    # 4782

    fibonacci = 1
    second = 0
    index = 1
    n = 1

    for i in range(999):
        n *= 10

    while fibonacci < n:
        fib = fibonacci+second
        second = fibonacci
        fibonacci = fib
        index += 1
    print(index)


def problem29():
    # Distinct Powers
    # 9183

    a = 2
    lista = []

    while a <= 100:
        b = 2
        while b <= 100:
            lista.append(a**b)
            b += 1
        a += 1
    print(len(set(lista)))
