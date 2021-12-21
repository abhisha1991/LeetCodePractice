#https://www.geeksforgeeks.org/given-binary-string-count-number-substrings-start-end-1/
def solve(s):
    count = 0
    for i in range(len(s)):
        if s[i] == '1':
            count +=1
    return count * (count-1) / 2

# we are selecting 2 '1' values from a count of N '1' values
# there are N choose 2 ways to do this ==> N choose 2 is nothing but N!/(N-2)! * 2! = N * (N-1) / 2