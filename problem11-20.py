def problem12():
    # Highly divisible triangular number

    divisors = []
    number = 0
    i = 0
    while len(divisors) < 501:
        i += 1
        number += i
        divisors = []
        for n in range(int(number/2)+1):
            if number % (n+1) == 0:
                divisors.append(n+1)
        divisors.append(number)
        print(number)
