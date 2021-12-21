# https://codefights.com/interview/xDa56krZhEx5BnvaA
def primesSum2(n):
    if n is 1:
        return 0
    sum = 2
    primes = [2]
    for i in range(2, n + 1):
        is_prime = True
        div_by_prime = False
        for p in primes:
            if (i % p == 0):
                div_by_prime = True
                break
        if (div_by_prime is True):
            is_prime = False
            continue
        if is_prime:
            primes.append(i)
            # print(primes)
            sum = sum + i

    mod = (10 ** 9) + 7
    return sum % mod


print(primesSum2(10))
