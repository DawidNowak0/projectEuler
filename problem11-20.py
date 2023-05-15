def problem12():
    divisors = []
    number = 0
    i = 0
    while len(divisors) < 501:
        i = i + 1
        number += i
        divisors = []
        for n in range(number+1):
            if number % (n+1) == 0:
                divisors.append(n+1)
        print(number)


problem12()
