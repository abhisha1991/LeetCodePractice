# https://leetcode.com/problems/subarray-sum-equals-k
# https://www.youtube.com/watch?v=fFVZt-6sgyo
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        # this dictionary holds the number of times we have seen the "sum so far", ie, "prefix sum"
        prefix_sum_count = defaultdict()
        # we have seen a sum of 0 once, ie, an empty prefix array
        prefix_sum_count[0] = 1
        
        sum_so_far = 0
        
        for i in nums:
            sum_so_far += i
            
            # this is the critical line
            if sum_so_far - k in prefix_sum_count.keys():
                result += prefix_sum_count[sum_so_far - k]
            
            # always add "sum so far" into prefix sum count dictionary
            # the dictionary is just saying that we have seen these many ways to obtain the current prefix sum
            if sum_so_far not in prefix_sum_count.keys():
                prefix_sum_count[sum_so_far] = 1
            else:
                prefix_sum_count[sum_so_far] += 1
                
        
        return result

'''
From leetcode:

The idea behind this approach is as follows: If the cumulative sum(represented by sum[i] for sum up to ith index) up to two indices is the same, 
the sum of the elements lying in between those indices is zero. 

Extending the same thought further, if the cumulative sum up to two indices, say i and j is at a difference of k 
i.e. if sum[i] - sum[j] = k, the sum of elements lying between indices i and j is k.

Based on these thoughts, we make use of a hashmap mapmap which is used to store the cumulative sum up to all the indices possible along with the number of times the same sum occurs. 
We store the data in the form: (sum_up_to_i, # occurrences of sum up to i)

We traverse over the array nums and keep on finding the cumulative sum. 
Every time we encounter a new sum, we make a new entry in the hashmap corresponding to that sum. 
If the same sum occurs again, we increment the count corresponding to that sum in the hashmap. 

Further, for every sum encountered, we also determine the number of times the sum sum-k has occurred already, 
since it will determine the number of times a subarray with sum k has occurred up to the current index. 
We increment the result by the same amount.

After the complete array has been traversed, the result gives the required value.
'''