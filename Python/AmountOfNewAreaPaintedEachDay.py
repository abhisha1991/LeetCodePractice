# https://leetcode.com/problems/amount-of-new-area-painted-each-day/
class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        '''
        store all intermediate steps in a dict. 
        so if you have [5, 8], your dict would contain {5 : 8, 6 : 8, 7 : 8}. 
        next time if you get [6, 9], you can just jump to 8 and continue.
        '''
        jump = dict()
        worklog = []
        
        '''
        consider the trace of  [[1,4],[4,7],[5,8],[10,12],[11,12]]
        jump = {}
        
        process [1,4]
        work = 0
        start = 1 is not in jump
        so jump[1] = 4, work = 1, start = 2
        start = 2 is not in jump
        so jump[2] = 4, work = 2, start = 3
        start = 3 is not in jump
        so jump[3] = 4, work = 3, start = 4
        start == end (so break) and add work=3 in result
        
        process [4,7]
        work = 0
        start = 4 not in jump
        so jump[4] = 7, work = 1, start = 5
        start = 5 not in jump
        so jump[5] = 7, work = 2, start = 6
        start = 6 not in jump
        so jump[6] = 7, work = 3, start = 7
        start == end (so break) and add work=3 in result
        
        process [5,8]
        work = 0
        start = 5 is in jump
        so start = jump[5], ie, start = 7
        start = 7 not in jump
        so jump[7] = 8, work = 1, start = 8
        start == end (so break) and add work=1 in result
        
        so while processing [5,8] we were able to jump 5,6 and directly go to 7
        
        process [10,12]
        work = 0
        start = 10 not in jump
        so jump[10] = 12, work = 1, start = 11
        start = 11 not in jump
        so jump[11] = 12, work = 2, start = 12
        start == end (so break) and add work=2 in result
        
        process [11, 12] <<<NOTICE HOW WE CAN PROCESS OVERLAPPING INTERVALS>>>
        this overlaps with [10,12] so we should ideally do 0 work
        work = 0
        start = 11 is in jump
        so start = jump[11], ie, start = 12
        start == end (so break) and add work=0 in result
        '''
        for start, end in paint:
            work = 0
            
            while start < end:
                if start in jump: 
                    start = jump[start]
                else:
                    jump[start] = end
                    # update work by one unit for this current interval
                    work += 1
                    # update start by 1 unit for this interval
                    start += 1
                    
            worklog.append(work)
                    
        return worklog