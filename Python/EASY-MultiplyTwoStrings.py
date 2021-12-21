# https://codefights.com/interview/At83id5ZCwo2mNzdm
def multiplyTwoStrings(s1, s2):
    s1_int = int(s1)
    s2_int = int(s2)
    return str(s1_int * s2_int)
    pass

multiplyTwoStrings("23", "34")

# https://www.youtube.com/watch?v=l65AaJTg6oQ&t=214s
def multiply(s1, s2):
    m = len(s1)
    n = len(s2)
    res = 0
    for i in range(m):
        a = int(s1[m - i - 1])
        for j in range(n):
            b = int(s2[n - j - 1])
            print("a and b are", a, b)
            temp = a * b * (10 ** (i + j))
            print("temp is", temp)
            res += temp
    return res

print(multiply("23", "34"))


'''
   30    4
20 600   80
3  90    12

23 x 34 = 782
600 + 90 + 80 +12 = 782

'''