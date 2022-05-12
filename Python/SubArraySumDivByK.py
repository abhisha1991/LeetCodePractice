# https://leetcode.com/problems/subarray-sums-divisible-by-k/
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        '''
        imagine you have k = 5 and array 
                            arr =    [4, 5, 0, -2, -3, 1]
        calculate prefix sum
                            prefix = [4, 9, 9,  7,  4, 5]
                                         |  |   |   |  |
                                         Si Sx Sy   Sj Sz  
        
        final ans for this is [5], [0], [5,0], [-2,-3], [0,-2,-3], [5,0,-2,-3], [4,5,0,-2,-3,1], ie, count = 7
        
        now Si % k = 4
        also, Sj % k = 4
        So neither are divisible by 5
        but if we take Sj - Si, ie, 9-4 =-5, ie, the sub array [5, 0, -2, -3], this is divisible by 5
        
        similarly, Sx % k = 4, not divisible by 5
        but if we take Sx - Si = 9-9 = 0, ie, subarray [5,0], this is divisible by 5
        
        in the same spirit, if we take 
        Sy % k = 2
        we need another 2 to remove from another prefix sum's modulo, so we can make the sub array divisible by 5
        we find there is no such prefix sum element whose value can be modulo with k to give us 2
        
        if we did Sy - Sz = 7-5 = 2, this subarray won't be divisible by 5, ie, sub array [-2,-3,1] not div by 5
        
        so in effect, we have to keep track of what the remainder is of each prefix sum element when modulo by k
        
        0 --> 1 -- is saying there is 1 element whose modulo with k is 0, (prefix[5]), remainder freq = 1
        1 --> 0
        2 --> 1
        3 --> 0
        4 --> 4
        
        now we can pick any 2 elements whose remainder is 4 (say Si and Sj) and we can form an subarray between them
        that is divisible by k=5, ie, [5,0,-2,-3]
        
        So if there are 3 instances where remainder is 4, we need to pick 2 of them -- so total ways we can do this is
        4 choose 2 = 4 x 3 / 2 = 6
        
        in general, n choose k =    n!     or          n choose 2 will be     n!     ==    n x (n-1)
                                ---------                                  ---------       ---------
                                (n-k)! k!                                  (n-2)! 2!           2
                                
        so we need to go through every element in the dictionary and do n choose 2 against its remainder frequency (n)
        special case for 0 remainder -- in addition to n choose 2 for 0, we need to add n (remainder frequency)
        why? because consider [0,0,5] and k=5, then count is 6, ie, [0], [0], [5], [0,0], [0,5], [0,0,5], which is 3c2 + 3
        the additional 3 is coming from individual elements that can be selected as answer, ie, [0], [0], [5], ie, 3c1
        '''
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
            
        dic = dict()
        for p in prefix:
            # note that if p was negative, its remainder is still positive in python
            # ie, -4 % 5 = 4 and 4 % 5 = 4
            remainder = p % k
            if remainder not in dic:
                dic[remainder] = 1
            else:
                dic[remainder] += 1
        
        count = 0
        for k,v in dic.items():
            # special case for 0
            if k == 0:
                count += v
            
            count += int(v * (v-1) / 2)
        
        return count