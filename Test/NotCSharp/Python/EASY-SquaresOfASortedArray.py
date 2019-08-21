#https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        l = 0
        r = len(A)-1
        lst=[]

        while l<=r:
            if (A[l]**2<A[r]**2):
                lst.append(A[r]**2)
                r-=1
            else:
                lst.append(A[l]**2)
                l+=1
        return lst[::-1]
