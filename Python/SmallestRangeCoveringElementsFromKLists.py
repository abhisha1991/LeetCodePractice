# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists
import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        if k == 1:
            return [nums[0][0], nums[0][0]]
        '''
        smallest range means that 
        [20, 25] is smaller than [20, 26] - obviously
        but
        [20, 25] is smaller than [21, 26] also,
        ie, even though size of ranges is same, the smaller one is the one which has smaller left boundary
        '''
        
        '''
        we will use k minheaps to track the min values from the k lists
        inputs are already sorted, as given in the question
        
        say we had these 3 lists given:
        n1 = [4, 10, 15, 24, 26]
        n2 = [0, 9, 12, 20]
        n3 = [5, 18, 22, 30]
        
        we have a pointer to each of the 3 lists, ie, [4,0,5] --> range for this is [0,5]
        now to decrease this range, we can either increase lower bound or decrease upper bound
        
        we cannot decrease upper bound actually since:
        1. we're at the start of each of the lists
        2. also, in general, even if we were not at the start, we cannot decrease upper bound since
           we'll always be at the lowest numbers since we're parsing left to right and list is sorted!
           
        so the idea is to maintain k heaps, get the min element from each and form a range
        and keep updating that range until one of the heaps is exhausted
        '''
        
        # create a list of min heaps
        # this will hold k minheaps
        heaps = []
        ans = []
        
        # this will hold current k numbers that are min numbers from each of the heaps
        # make this also a heap since we would need to eject out smallest element from it often
        vals = []
        heapq.heapify(vals)
        
        # creake k heaps
        for n in nums:
            heapN = list(n)
            
            heapq.heapify(heapN)
            heaps.append(heapN)
        
        # populate vals and ans initially
        for h in heaps:
            heapq.heappush(vals, h[0])
            
        maxVal = max(vals)
        minVal = min(vals)
        ans = [minVal, maxVal]

        # flag tracks the emptiness of a heap
        # the moment a single heap becomes empty, we must exit
        # why? because the range should belong to all lists
        flag = False
                
        while True:
            for h in heaps:
                # if any of the heaps becomes empty, we exit out
                # we need an element from each heap every time
                if not h:
                    flag = True
                    break
                else:
                    # if current min range val is what the current heap's min val is
                    # then increase lower bound of this heap
                    if minVal == h[0]:
                        # pop this min val
                        heapq.heappop(h)
                        if not h:
                            flag = True
                            break
                        
                        # add next minval from this heap 'h', which is of course larger than h[0] above
                        # since we did a pop of the heap
                        heapq.heappush(vals, h[0])
                        
                        # remove the smallest value from vals 
                        # (remove will be an o(1) operation in a heap)
                        # this value that is taken out should be the current minVal
                        x = heapq.heappop(vals)
                        assert(x == minVal)
                        
                        maxVal = max(vals)
                        minVal = min(vals)
                        
                        # update ans range if needed
                        oldRange = ans[1] - ans[0]
                        newRange = maxVal - minVal
                        if (oldRange > newRange) or (oldRange == newRange and minVal < ans[0]):
                            ans = [minVal, maxVal]
            
            # exit out of outer loop
            if flag:
                break
        
        return ans