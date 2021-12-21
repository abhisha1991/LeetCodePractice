# The original problem is - count the numbers without consecutive 1s
# https://www.youtube.com/watch?v=a9-NtLIs1Kk&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=39
'''
for example, in (2^3) - 1's binary representation
we have,
111
110
101 -- X
100 -- X
011
010 -- X
001 -- X
000 -- X
Here the number of instances where we dont have consecutive 1s are marked with an X, ie - 5
How to find this? Tushar has a great explanation in his video above
'''
dic = dict()
def nums_wo_consecutive_1(n):
    x = pow(2, n) - 1
    print("The number is", x)
    return fib(n)

def fib(n):
    dic[0] = 0
    dic[1] = 2
    dic[2] = 3
    dic[3] = 5
    if n in dic.keys():
        return dic[n]
    dic[n] = fib(n - 1) + fib(n - 2)
    return dic[n]

print(nums_wo_consecutive_1(5))
print(nums_wo_consecutive_1(4))