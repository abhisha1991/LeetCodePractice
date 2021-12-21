# https://leetcode.com/problems/interval-list-intersections/ - trace this with original example to understand solution below
class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        lenA = len(A)
        lenB = len(B)
        
        i = 0
        j = 0
        res = []
        while (i < lenA and j < lenB):
            a = A[i]
            b = B[j]
            
            # try and find an intersection
            startmax = max(a[0], b[0])
            endmin = min(a[1], b[1])
            
            # if the intersection has start and end that are valid
            # notice the equal to as well, so this includes intervals like [5,5]
            if endmin >= startmax:
                res.append([startmax, endmin])
                
            # update i and j, based on endmin - whoever has reached the end
            if endmin == a[1]:
                i +=1
            if endmin == b[1]:
                j +=1
        
        return res

# here's an attempt that didnt work - lost the code unforuntately:
'''
high level explanation:
1. create an array 'arr1' where we will fill a spot with 'a' if it is in the intervals of A
2. create an array 'arr2' where we will fill a spot with 'b' if it is in the intervals of B 
3. if we have a spot outside of the ranges marked in A or B, then fill those spots in arr1 and arr2 with 'x'

So the example in the original case becomes:
A = [[0,2], [5,10], [13,23], [24,25]]
B = [[1,5], [8,12], [15,24], [25, 26]]
Ans = [1,2], [8,10], [15,23], [24,24], [25,25]

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
a a a x x a a a a a a  x  x  a  a  a  a  a  a  a  a  a  a  a  a  a  x  <--- arr1
x b b b b b x x b b b  b  b  x  x  b  b  b  b  b  b  b  b  b  b  b  b  <--- arr2

Now the intersection becomes all those start / end points where we have both 'a' and 'b'
[1,2], [5,5], [8,10], [15,25]
This works great for the most part, except that it loses the ability to partition on the basis of intervals, like [15, 25].
The correct partition should have been [15,23], [24,24], [25,25]

'''