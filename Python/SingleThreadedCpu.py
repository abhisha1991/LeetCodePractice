# https://leetcode.com/problems/single-threaded-cpu/
from heapq import *
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # add idx of the task along with their enqueue time and processing time
        tasks = [(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))]
        # sort by enqueue time and processing time
        tasks = sorted(tasks, key=lambda x: (x[0], x[1]))
        
        if not tasks:
            return []
        
        minh = []
        heapq.heapify(minh)
        
        # initialize the cpu timer (clock) as the enqueue time for the first task
        timer = tasks[0][0]
        res = []
        
        i = 0
        
        while minh or i < len(tasks):
            # while there are tasks and the current timer is greater than the enqueue time of the current task
            while i < len(tasks) and timer >= tasks[i][0]:
                # only add process time and id to the heap
                heapq.heappush(minh, (tasks[i][1], tasks[i][2]))
                i +=1
            
            # this is important, ie, to advance the timer so you can keep adding tasks in case you're unable to
            # increment timer via the path of min heap (else condition)
            if not minh:
                timer = tasks[i][0]
            else:
                # pop from heap (pop order will be based on smallest processing time, smallest process idx)
                # and after popping, process the tasks and increase the timer
                processTime, idx = heapq.heappop(minh)
                res.append(idx)
                timer += processTime
                
        return res