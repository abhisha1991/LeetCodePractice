# https://leetcode.com/problems/4sum-ii/description/
class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        num_dict = dict()
        # this dictionary will hold the sum for lists C and D and the number of times that sum occurred
        for c in C:
            for d in D:
                i = c + d
                if i in num_dict.keys():
                    num_dict[i] +=1
                else:
                    num_dict[i] = 1

        count = 0
        for i in range(len(A)):
            for j in range(len(B)):
                target = 0 - (A[i] + B[j])
                # we are looking for target in the dictionary
                if target in num_dict.keys():
                    # if it was found, then this target when paired with any of the c,d that added to target will give 0
                    # hence we increase the count by the value of the dict
                    count += num_dict[target]
        return count
