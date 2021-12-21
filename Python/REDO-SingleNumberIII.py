# https://leetcode.com/problems/single-number-iii/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        setx = set(nums)
        sety = set(nums)
        for i in nums:
            if i in setx:
                setx.remove(i)
                continue
            if i in sety:
                sety.remove(i)
        return list(sety)

'''
input:[1,2,1,3,2,5]
ans should be [3,5]
create 2 sets = which contain a distinct set of nums
1st iteration:
i=1
1 is in setx, so remove 1, setx = (2,3,5)
2nd iteration:
i=2
2 is in setx, so remove 2, setx = (3,5)
3rd iteration
i=1
1 is NOT in setx, so remove 1 from sety, sety = (2,3,5)
4th iteration
i=3
3 is in setx, so remove 3, setx =(5)
5th iteration
i=2
2 is NOT in setx, so remove 2 from sety, sety = (3,5)
6th iteration
i=5
5 is in setx, so remove 5, setx = ()

return sety = (3,5)
'''