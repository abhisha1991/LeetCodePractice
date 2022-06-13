# https://leetcode.com/problems/maximum-performance-of-a-team/
from heapq import *
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10**9 + 7
        eng = [(speed[i], efficiency[i]) for i in range(n)]
        # sort by decreasing efficiency, ie, highest efficiency person first
        eng = sorted(eng, key=lambda x: -x[1])
        if k == 0:
            return 0
        
        '''
        we have sorted the list based on decreasing efficiency, ie, engineers more efficient than the 'i'th engineer
        are to the left of the 'i'th engineer
        
        the idea here is that we iterate through the list of engineers and pick the 'i'th person by default
        now we need to pick (at most) k-1 more people to complete the team
        
        say if we pick the 'i'th engineer by default, then say this 'i'th engineer forms the baseline in terms of efficiency
        ie, the rest of the team will be made of engineers more efficient than this engineer, ie, the rest of the team comes from
        the left of the array of position 'i'
        
        that way, we are making a guarantee that we have fixed on a minimum efficiency on the team, ie, efficiency of person i -
        now for the speed, we need to try and pick at most k-1 people from the left array, they have the higher efficiency (we know)
        but we want to pick the k-1 highest speed engineers
        
        we also want to try and pick maximum number of people (up to k-1) since more people means more speed added to our total speed
        
        so we can maintain a max heap and have its size be k-1 max, that way we can keep track of k-1 engineers with highest speeds
        who are more efficient than our baseline engineer 'i'
        
        alternatively, we can have a min heap, and we keep its size as k-1 and we keep ejecting from it if it hits capacity
        '''
        
        # holds the top k-1 speed engineers
        pq = []
        heapq.heapify(pq)
        
        speedSumSoFar = 0
        mxperf = 0
        for i in range(n):
            curr = eng[i]
            
            speed = curr[0]
            eff = curr[1]

            speedSumSoFar += speed
            
            if len(pq) > k-1:
                slowest = heapq.heappop(pq)
                speedSumSoFar -= slowest
            
            # ingest current speed into heap
            heapq.heappush(pq, speed)
            
            # we already established that min efficiency will be current engineer's efficiency
            mxperf = max(mxperf, eff * speedSumSoFar)
            # below is inefficient of course, since sum(pq) takes o(k) time, but the below and above are equivalent statements
            # mxperf = max(mxperf, eff * sum(pq))
        
        return mxperf % mod