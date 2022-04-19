class Solution:
    # https://www.youtube.com/watch?v=rZLvA1rsLy4
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        jobs = sorted(jobs, key = lambda x: (x[0]))
        
        # print(f"jobs is {jobs}")
        N = len(jobs)
        
        # this component is key, we need to lru_cache this, else we get TLE
        @lru_cache(None)
        def maxProfits(i):
            if i >= N:
                return 0
            
            curEnd = jobs[i][1]
            curProfit = jobs[i][2]
            
            # get the next job right after this current job ends 
            j = i+1            
            while j < N:
                startNxt = jobs[j][0]
                if curEnd > startNxt:
                    j +=1
                else:
                    break
            
            # either dont do current job and look in the future, 
            # or take current job and explore job that starts immediately after this one
            return max(0 + maxProfits(i+1), curProfit + maxProfits(j))
        
        return maxProfits(0)

    # this is o(n2) solution since we have to iterate over dictionary every time
    def jobScheduling2(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        
        jobs = sorted(jobs, key = lambda x: (x[0], x[1]))

        # end time to "max profit at end time" map
        jobProfit = dict()
        jobProfit[0] = 0 
        mxprofit = 0 
        
        for i in range(len(jobs)):
            selected = jobs[i][2]
            notSelected = 0
            
            start = jobs[i][0]
            end = jobs[i][1]
            
            # max profit variables
            val1 = 0 # select job, and add to max profit (up to) just before this job started
            val2 = 0 # do not select job, and add max profit (up to) just before this job ended
            
            for k,v in jobProfit.items():
                if k <= start and val1 < v:
                    val1 = v
                if k <= end and val2 < v:
                    val2 = v
                    
            selected += val1
            notSelected += val2
                
            mxprofit = max(selected, notSelected)
            # print(f"Processing start and end: {start},{end}. Max profit is {mxprofit}")
            jobProfit[end] = mxprofit
        
        return max(jobProfit.values())