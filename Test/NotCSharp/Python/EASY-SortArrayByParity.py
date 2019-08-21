#https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even_arr = []
        odd_arr = []
        for x in A:
            if x%2==0:
                even_arr.append(x)
            else:
                odd_arr.append(x)
        return even_arr+odd_arr
