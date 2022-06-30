# https://leetcode.com/problems/product-of-two-run-length-encoded-arrays
class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        # pointers to encoded1 and encoded2
        i = 0
        j = 0
        
        # frequencies
        f1 = 0
        f2 = 0
        
        # values
        v1 = 0
        v2 = 0
        
        m = len(encoded1)
        n = len(encoded2) 
        ans = []
        
        while i < m or j < n:     
            # get the values in f1, v1 and f2, v2
            # our condition of "picking the next value" is when i or j is a valid index (of course)
            # AND IF the corresponding freq is 0
            if f1 == 0 and i < m:
                v1, f1 = encoded1[i]
                
            if f2 == 0 and j < n:                     
                v2, f2 = encoded2[j]
            
            # calculate smaller frequency and product
            fmin, product = min(f1, f2), v1 * v2  
            
            # if current product is the same as previous one, update previous frequency
            if ans and ans[-1][0] == product:        
                ans[-1][1] += fmin
                
            else:
                # other situation, append new pairs
                ans.append([product, fmin])
            
            # deduct both f1 and f2 by fmin
            # one (or both) of them will become 0 now
            f1 -= fmin
            f2 -= fmin
            
            # remember, we increment i and j based on whether freq is 0
            # this is the criteria used when determining whether to pick the next element or not
            if f1 == 0:
                i +=1
            
            if f2 == 0:
                j +=1
                
        return ans