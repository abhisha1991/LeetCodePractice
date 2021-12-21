# https://leetcode.com/problems/stone-game/
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        if n == 0:
            return False
        
        arr = [[None] * n for y in range(n)]
        for i in range(n):
            arr[i][i] = [piles[i], 0]
                    
        
        # traverse the 2d matrix diagnol wise
        l = 1
        while l <= n:
            i = 0
            j = l
            while j < n:
                p =  piles[i:j+1]
                # pick from beginning of pile
                option1 = piles[i] + arr[i+1][j][1]
                # pick from end of pile
                option2 = piles[j] + arr[i][j-1][1]
                    
                first = max(option1, option2)
                if option1 > option2:
                    # second player is you, ie, index 0, in that case, because you've made your pick
                    second = arr[i+1][j][0]
                else:
                    # second player is you, ie, index 0, in that case, because you've made your pick
                    second = arr[i][j-1][0]
                        
                arr[i][j] = [first, second]
                j +=1
                i +=1
            l +=1
        
        # check if player 1 won by having a larger score
        return arr[0][n-1][0] > arr[0][n-1][1]