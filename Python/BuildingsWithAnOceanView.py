# https://leetcode.com/problems/buildings-with-an-ocean-view 
from collections import defaultdict
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxright = []
        # h2idx is a dictionary that stores the indexes corresponding to a max height seen
        h2idx = defaultdict(list)
        maxh = -sys.maxsize
        n = len(heights)
        
        # go from right to left
        for i in range(n-1,-1,-1):
            if maxh < heights[i]:
                maxh = heights[i]
                # we add to the dictionary here, the key being the maxh we just found
                # value being a list of indices from the right of the arr where
                h2idx[maxh].append(i)
            
            maxright.append(maxh)
        
        # we need to reverse because we appended to the arr left to right
        # while we were parsing the arr right to left
        maxright.reverse()
        
        result_idx = []
        # notice how we will return the asc order of indices since we're going left to right
        # notice that we're traversing only 0 to n-2, last building will always have ocean view
        for i in range(n-1):
            # this is the critical piece
            # we must be greater than our maxright nbor
            # the equality is being held in case we ourselves were the tallest
            # since maxright was calculated as inclusive of the current building
            
            # the second criteria is very important
            # we're saying that if the 1st condition (heights[i] >= maxright[i]) was met
            # we are guaranteed to be in h2idx as a key
            # now we want to ensure that there are no indices on the right of us whose height
            # is equal to us, else our view will be blocked!
            if heights[i] >= maxright[i] and h2idx[heights[i]][0] <= i:
                result_idx.append(i)
        
        # right most building can always see the ocean
        result_idx.append(n-1)
        return result_idx