#http://www.geeksforgeeks.org/?p=12635
import time


# Memoized solution
fib_dict = dict()
def fib1(n):
    if n <= 1:
        return n
    if n - 1 not in fib_dict.keys():
        fib_dict[n-1] = fib1(n-1)
    if n - 2 not in fib_dict.keys():
        fib_dict[n-2] = fib1(n-2)
    return fib_dict[n-1] + fib_dict[n-2]

tic = time.time()
print(fib1(30))
print(fib_dict)
toc = time.time()

print("Memoized solution took: " + str((toc - tic) * 1000))

# Tabulated solution
def fib2(n):
    f = dict()
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

tic = time.time()
print(fib2(30))
toc = time.time()
print("Tablulated solution took: " + str((toc - tic)* 1000))

# Recursive solution
def fib3(n):
    if n <=1:
        return n
    return fib3(n-1) + fib3(n-2)

tic = time.time()
print(fib3(30))
toc = time.time()
print("Normal recursive solution took: " + str((toc - tic)* 1000))
