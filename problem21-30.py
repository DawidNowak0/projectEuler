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
