# https://leetcode.com/problems/exclusive-time-of-functions/
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # stores (pid) for a given process entry
        # added to stack only during start of process
        stack = []
        def parse(log):
            arr = log.split(":")
            arr = [int(arr[0]), arr[1], int(arr[2])]
            return tuple(arr)
        
        logs = [parse(i) for i in logs]
        
        i = 0
        # key is pid and value is total time for this pid
        ptime = dict()
        maxend = 0
        
        while i < len(logs):
            pid, action, ts = logs[i]
            if pid not in ptime:
                ptime[pid] = 0
                
            if action == 'start':
                if stack:
                    # for prev pid, lock in time
                    prev = stack[-1]
                    # current process start time (ts) acts as a temporary end time for prev process, 
                    # so we can capture this time delta at least
                    ptime[prev] += ts - maxend
                    
                maxend = ts
                stack.append(pid)
                
            
            # if we process we're ending is matching the one that started and is on top of stack
            elif stack[-1] == pid:
                stack.pop()
                # why ts+1? because end is indicating the ts when something starts to end
                # the real end time is going to be ts+1
                ptime[pid] += ts + 1 - maxend
                maxend = ts + 1
                
            i +=1
        
        ans = []
        mx = max(ptime.keys())
        # mx+1 because we want to include process with id = mx
        for i in range(mx+1):
            ans.append(ptime[i])
        return ans