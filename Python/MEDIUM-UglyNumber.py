#http://www.geeksforgeeks.org/?p=753
import time

def uglyNumber(n):
    uglyNums = list()
    uglyNums.append(1)
    divs = [2, 3, 5]
    i = 2
    while len(uglyNums) < n:
        j = i
        for x in divs:
            while j % x == 0:
                j = j / x
        if j == 1:
            #print(i)
            uglyNums.append(i)
        i = i + 1

    return uglyNums[len(uglyNums) - 1]

#1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15
tic = time.time()
print(uglyNumber(1000))
toc = time.time()
print("My solution took: " + str((toc - tic)* 1000))


# Geeks for geeks solution
# Uses Memoization, stores the values of the previous ugly numbers in the list,
# thereby deriving the new number from the old one
def getNthUglyNo(n):
    ugly = [0] * n  # To store ugly numbers

    # 1 is the first ugly number
    ugly[0] = 1

    # i2, i3, i5 will indicate indices for 2,3,5 respectively
    i2 = i3 = i5 = 0

    # set initial multiple value
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    # start loop to find value from ugly[1] to ugly[n]
    for l in range(1, n):

        # choose the min value of all available multiples
        ugly[l] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)

        # increment the value of index accordingly
        if ugly[l] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2

        if ugly[l] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3

        if ugly[l] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5

    # return ugly[n] value
    return ugly[-1]

tic = time.time()
print(getNthUglyNo(1000))
toc = time.time()
print("G4G solution took: " + str((toc - tic)* 1000))