# https://leetcode.com/problems/maximum-swap/
class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num
        
        snum = str(num)
        
        # holds num digit and its last index found in the array
        dic = dict()
        for i in range(len(snum)):
            n = int(snum[i])
            if n not in dic:
                dic[n] = i
            else:
                if i > dic[n]:
                    dic[n] = i
        
        # convert to a list, so we can swap
        snum = list(snum)
        swap = False
        # max key is going to be the max digit we saw in the number
        # by default, we would want this to be 9 (as a number could potentially have 9 as the highest digit)
        mxkey = max(dic.keys())
        
        for i in range(len(snum)):
            cur = int(snum[i])
            # only 1 swap allowed, if already swapped, break
            if swap:
                break
            
            # go from max digit to cur+1 (note that for loop iteration does cur+1 and not cur)
            for j in range(mxkey, cur, -1):
                if j in dic:
                    # if we find a digit that is larger than our current digit
                    # then swap the place of this larger digit with your current digit
                    lastidx = dic[j]
                    if lastidx > i:
                        tmp = snum[i]
                        snum[i] = snum[lastidx]
                        snum[lastidx] = tmp
                        # only 1 swap allowed, so mark flag as true
                        swap = True
                        break
        
        # snum was a list of chars, so convert back to int
        return int(''.join(snum))