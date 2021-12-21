# https://leetcode.com/problems/sort-array-by-parity-ii/solution/
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = 1
        even = 0
        dic = dict()
        for i in A:
            if i % 2 == 0:
                dic[even] = i
                even += 2
            else:
                dic[odd] = i
                odd += 2
        
        return [dic[x] for x in range(len(A))]
    
        