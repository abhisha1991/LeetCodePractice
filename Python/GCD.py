def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


print(gcd(30, 1))
print(gcd(120, 30))
print(gcd(1, 30))
print(gcd(150, 15))

