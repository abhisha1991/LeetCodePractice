# https://leetcode.com/problems/strobogrammatic-number
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        dic = dict()
        dic['0'] = '0'
        dic['1'] = '1'
        dic['6'] = '9'
        dic['8'] = '8'
        dic['9'] = '6'
        
        l = 0
        r = len(num)-1
        while l <= r:
            # a number like 1234
            # will fail on evaluating digit 2, because 2 cannot be 'mirrored'
            if num[l] not in dic:
                return False
            
            # it is potentially mirror-able
            # now we need to check if this left number's mirror is the right number
            # say we had 69 --> then 6's mirror is 9, which is equal to what we are evaluating from the right
            # so this number 69 is strobogrammatic, if we had something like 60 -- then it wouldn't be, because we need to have 6's mirror on the right!
            n = num[l]
            if dic[n] != num[r]:
                return False
            
            l +=1
            r -=1
        return True