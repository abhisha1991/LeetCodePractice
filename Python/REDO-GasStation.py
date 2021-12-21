# https://discuss.leetcode.com/topic/27760/possibly-the-most-easiest-approach-o-n-one-variable-python
'''
The algorithm is pretty easy to understand.
Imagine we take a tour around this circle, the only condition that we can
complete this trip is to have more fuel provided than costed in total. That's what the first loop does.

If we do have more fuel provided than costed,
that means we can always find a start point around this circle that we could complete
the journey with an empty tank. Hence, we check from the beginning of the array,
if we can gain more fuel at the current station, we will maintain the start point, else,
which means we will burn out of oil before reaching to the next station, we will start over at the next station.
'''
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        lengas = len(gas)
        lencost = len(cost)
        if lengas != lencost:
            return -1
        if lengas is 0:
            return -1

        gasleft = 0
        for i in range(lengas):
            gasleft += gas[i] - cost[i]

        # we wont have enough gas if we went through all the stops
        if gasleft < 0:
            return -1

        start = 0
        gasleft = 0
        # we will have gasleft > 0 at this point, now we just need to find start
        '''
        Next, accumulate the "surplus" or "deficit" along the circle, at one point, you will have the biggest deficit. 
        Starting from the next station, you will never run into deficit so you can travel around the circle.
        '''
        for i in range(0, lengas):
            gasleft += gas[i] - cost[i]
            if gasleft < 0:
                gasleft = 0
                # why do we claim that start = i+1 will be the best position to start if gasleft < 0
                # there is a mathematical proof around this
                start = i + 1
        return start