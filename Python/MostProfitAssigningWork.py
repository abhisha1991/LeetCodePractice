class Solution:
    # this is o(nlogN) solution as it does binary search, this is more straight forward to understand
    def maxProfitAssignment2(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        dprofit = dict()
        maxProfitPrefix = []
        
        # map the difficulty to the max profit possible
        for i in range(len(profit)):
            d = difficulty[i]
            if d not in dprofit:
                dprofit[d] = profit[i]
            else:
                if dprofit[d] < profit[i]:
                    dprofit[d] = profit[i]
        
        # sort the difficulties in asc order
        df = sorted(dprofit.keys())
        # have a dictionary mapping the difficulty to its corresponding index in the df list
        dfIdx = dict()
        for i in range(len(df)):
            dfIdx[df[i]] = i
        
        # stores the max profit prefix up to a given difficulty level
        # for example, if difficulty array is [10, 11, 12] and profit is [100, 90, 80] -- then for a person whose difficulty threshold is 20
        # we may mistakenly choose the highest difficulty available (12) even though it has less profit potential (80), compared to a choosing a lower
        # difficulty (10) that has higher profit potential (100). So if we had a prefix max array like [100, 100, 100], then we can overcome this less optimal choice!
        # this is needed in the binary search implementation
        for i in range(len(df)):
            # dfVal is the difficulty value
            dfVal = df[i]
            if i == 0:
                maxProfitPrefix.append(dprofit[dfVal])
                continue
            else:
                maxProfitPrefix.append(max(dprofit[dfVal], maxProfitPrefix[-1]))
                
            
        def binsearch(num, low, high, mp):
            if low > high:
                return mp
            
            mid = (low+high)//2
            if num < df[mid]:
                return binsearch(num, low, mid-1, mp)
            
            # get the difficulty value corresponding to mid index
            d = df[mid]
            # find the index for that "difficulty value (d)" in the df list
            idx = dfIdx[d]
            
            # find max profit, comparing current max profit with profit prefix for that index
            mp = max(mp, maxProfitPrefix[idx])
            # do binary search on the other half
            return binsearch(num, mid+1, high, mp)
        
        maxprofit = 0
        for w in worker:
            maxprofit += binsearch(w, 0, len(df)-1, 0)
        
        return maxprofit

    # this is o(n) solution but uses lots of space
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        maxProfitPrefix = [0] * 100000
        dset = set(difficulty)
        dprofit = dict()
        
        # map the max profit against a given difficulty
        for i in range(len(profit)):
            d = difficulty[i]
            p = profit[i]
            if d not in dprofit:
                dprofit[d] = p
            else:
                if p > dprofit[d]:
                    dprofit[d] = p
        
        # populate max profit prefix which stores maximum profit for a given difficulty i (index i is difficulty number)
        for i in range(len(maxProfitPrefix)):
            if i == 0 and i in dset:
                maxProfitPrefix[i] = dprofit[0]
                continue
                    
            elif i not in dset:
                maxProfitPrefix[i] = maxProfitPrefix[i-1]
            elif i in dset:
                maxProfitPrefix[i] = max(maxProfitPrefix[i-1], dprofit[i])
        
        total = 0
        for w in worker:
            total += maxProfitPrefix[w]
        return total