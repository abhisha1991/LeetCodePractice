# https://leetcode.com/problems/gas-station
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [gas[i]-cost[i] for i in range(len(gas))]
        
        # if total cost out weights the total gas, we won't be able to have a soln
        if sum(diff) < 0:
            return -1
        
        # now we know that there is more gas than cost, so a soln is possible
        # we just need to find the start index
        
        # also note, there is only ONE start point 
        # which is the earliest point with which we were able to complete the arr pass
        # without having total go down to less than 0 
        # https://www.youtube.com/watch?v=lJwbPZGo05A
        total = 0
        start = 0
        for i in range(len(diff)):
            total += diff[i]
            if total < 0:
                # we know current i is not start (since total starting at i < 0), 
                # so set it to i+1
                start = i + 1
                total = 0
        
        # this is the starting position such that the total never dipped below 0
        # starting from this starting pos
        return start