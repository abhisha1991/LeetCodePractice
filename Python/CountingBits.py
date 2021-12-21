# great solution: https://leetcode.com/problems/counting-bits/discuss/270693/Intermediate-processsolution-for-the-most-voted-solution-i.e.-no-simplificationtrick-hidden 

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0] * (num + 1) # we want to calculate res for [0,num]
        # for the number 0, there are no 1s in its representation, so we start the iteration from 1
        
        for i in range(1, num + 1):
            if i % 2 == 0: # if its an even number, then countBits(i) = countBits(i >> 1)
                res[i] = res[i >> 1]
            else: # if its an odd number, then countBits(i) = countBits(i >> 1) + 1 [as last digit is 1, so we add 1]
                res[i] = res[i >> 1] + 1
        return res
                
        