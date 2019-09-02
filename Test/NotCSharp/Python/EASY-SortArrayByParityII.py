#https://leetcode.com/problems/sort-array-by-parity-ii/submissions/

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        lst = [0]*len(A)
        m = 0
        q = 1

        for i in range(len(A)):
            if A[i]%2==0:
                lst[m]=A[i]
                m+=2
            else:
                lst[q]=A[i]
                q+=2

        return lst
