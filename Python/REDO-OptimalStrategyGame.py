'''
the second player is attempting to use the same optimal strategy as player one. So, after player one picks from the
left most or right most entry, player two will have the opportunity to attempt to maximize their return.

The values stored in the array are are stored in pairs where the first value in the pair is the maximum
value that the person currently picking can get and the second value is the maximum value that the person going after can get. 

Since it's player two's turn at that point, the player will naturally grab the first value in the pair and the player one, 
who will be the next one to go will be forced to grab the second value in the pair.
'''
# https://leetcode.com/problems/predict-the-winner/
# https://www.youtube.com/watch?v=WxpIHvsu1RI
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        '''
        nums = [3,9,1,2]

            1      2      3      4
        1 (3,0)   (9,3)   (4,9)  (11,4)
        
        2         (9,0)   (9,1)  (10,2)  
        
        3                 (1,0)  (2,1)
        
        4                        (2,0)
        
        fill arr in anti diagonal pattern
        '''
        n = len(nums)
        res = [[None] * n for i in range(n)]
        
        # picking range of nums from start = i and end = i, ie, only 1 number
        # first player always wins by picking up the number, as a result player 2 gets nothing
        for i in range(n):
            res[i][i] = (nums[i], 0)
        
        # l is length of sub array we will be playing the game with
        # we will consider all 1 length, 2 length, 3 length and so on sub arrays
        l = 1
        while l <= n:
            i = 0
            j = l
            while j < n:
                left = res[i][j-1]
                bottom = res[i+1][j]
                
                # player 1 has 2 options - either pick from the front or from the back
                # 1. choosing starting element (i) and then choosing the best you can do with [i+1, j] (exclude the ith) -- ie, leftover from 'bottom'
                # 2. choosing the ending element (j) and then choosing the best you can do with [i, j-1] (exclude the jth) -- ie, leftover from 'left'
            
                option1 = nums[i] + bottom[1]  # pick from front
                option2 = nums[j] + left[1]    # pick from end
                first = max(option1, option2)  # maximize player 1 score

                # if player 1 picked from the front, ie, they choose nums[i], ie, option1
                # then player 2 gets dibs on bottom, which is from i+1 to j
                if option1 > option2:
                    second = bottom[0]
                else:
                    # player 1 picked from back, ie, they chose nums[j], ie, option2
                    # then player 2 gets dibs on left, which is from i to j-1
                    second = left[0]
                    
                res[i][j] = (first, second)
                
                # increment inner loop
                i +=1
                j +=1
            
            # outer loop
            # consider next biggest sub array
            l +=1
        
        # ans is stored at res[0][n-1] since that consideres the entire length of nums
        first = res[0][n-1][0]
        second = res[0][n-1][1]
        if first >= second:
            return True
        return False