# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/
class Solution:
    # this runs in o(n) time
    def minSwaps(self, data: List[int]) -> int:
        win = data.count(1)
        # there's only a single 1 in the array, so no swaps are needed
        if win == 1:
            return 0
        
        i = 0
        # currOnes is tracking number of 1s in current window
        # maxOnes is tracking max number of 1s across any window (the largest cluster of 1s in a window)
        # answer is going to be total number of 1s in data - maxOnes (these are the number of 0s that we need to swap)
        currOnes = data[:win].count(1)
        maxOnes = data[:win].count(1)
        
        # go from win index to end of array
        # why? since we've already traversed the first window above
        for i in range(win, len(data)):
            # this sliding window is creating a truth table of the current element to add (data[i])
            # and the element to remove from the left of window, ie, (data[i-win])
            '''
            data[i]     data[i-win]   Effect on currOnes
              1              1        no effect
              1              0        add to currOnes
              0              1        subtract from currOnes
              0              0        no effect
            '''
            if data[i] == 1 and data[i-win] == 0:
                currOnes +=1
                if currOnes > maxOnes:
                    maxOnes = currOnes
            
            elif data[i] == 1 and data[i-win] == 1:
                # we need to add and subtract from currOnes, so effect is cancelled out
                pass
            
            elif data[i] == 0 and data[i-win] == 1:
                # we are removing 1 from the left
                # we are adding a 0 from the right
                currOnes -=1
            
            elif data[i] == 0 and data[i-win] == 0:
                # we are removing 0 from the left, and adding 0 to the right
                # so currOnes is not affected
                pass
            
        # win is the total number of 1s in the data array
        return win - maxOnes
                
    
    # this is slow because we have to iterate through all windows
    # for each window we have to count number of 0s, so its o(num_windows x num_zeros_in_window)
    def minSwaps2(self, data: List[int]) -> int:
        win = data.count(1)
        i = 0
        swap = sys.maxsize
        while i + win <= len(data):
            arr = data[i:win+i]
            if arr.count(0) < swap:
                swap = arr.count(0)
            i +=1
            
        return swap