# https://leetcode.com/problems/gas-station
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [gas[i]-cost[i] for i in range(len(gas))]
        
        # if total cost out weights the total gas, we won't be able to have a soln
        if sum(diff) < 0:
            return -1
        
        # now we know that there is more gas than cost, so a soln is possible
        # we just need to find the start index
        
        # also note, there is only ONE start point per the final answer, there cannot be 2 start indices
        # this will be the earliest point with which we were able to complete the arr pass
        # without having tank go down to less than 0 
        # https://www.youtube.com/watch?v=lJwbPZGo05A
        tank = 0
        start = 0
        for i in range(len(diff)):
            tank += diff[i]
            if tank < 0:
                # we know current i is not start (since tank starting at i < 0), 
                # so set it to i+1
                start = i + 1
                tank = 0
        
        # this is the starting position such that the tank never dipped below 0
        # starting from this starting pos
        return start