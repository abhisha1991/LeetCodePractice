# http://www.geeksforgeeks.org/count-number-of-ways-to-cover-a-distance/
dic = dict()


def number_of_ways(n):
    if n == 1:
        dic[1] = 1
        return 1
    if n == 2:
        dic[2] = 2
        return 2
    if n == 3:
        dic[3] = 4
        return 4
    if n in dic.keys():
        return dic[n]
    else:
        dic[n] = number_of_ways(n-1) + number_of_ways(n-2) + number_of_ways(n-3)
        return dic[n]

t = int(input())
for i in range(t):
    n = int(input())
    number_of_ways(n)
    print(dic[n])