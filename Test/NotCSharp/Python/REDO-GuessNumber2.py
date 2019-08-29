# https://leetcode.com/problems/guess-number-higher-or-lower-ii/submissions/
class Solution(object):    
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [[0 for x in range(n+1)] for y in range(n+1)]
        # we want the worst case money in hand when playing game with start=1, end=n, ie table[1][n]
        return self.dp(table, 1, n)

    def dp(self, table, start, end):
        if start >= end:
            # if start == end, you've guessed the number correctly, so $0 payout
            # if start > end, you cannot pick a number, so $0 penalty
            return 0 
        # if it already has a value, then return that value
        if table[start][end] != 0:
            return table[start][end]
        # start with max possible payout
        res = sys.maxsize
        for x in range(start, end+1):
            # find local minima by guessing x (which is the wrong guess), so you pay $x PLUS
            # either penalty when x was guessed higher than actual (start,x-1)
            # or penalty when x was guessed lower than actual (x+1, end)
            localmin = x + max(self.dp(table, start, x-1), self.dp(table, x+1, end))
            # res will contain global minima after this loop ends
            print("localmin is {0} for x {1} + max(dp({2},{3}), dp({4},{5})) with start={6} and end={7}".format(localmin, x, start, x-1, x+1, end, start, end))
            res = min(localmin, res)
        
        # assign global minima to the start end index element for table
        # read as "you will need atleast $ res for worst case guessing for start, end"
        table[start][end] = res
        print("res is {0} when start is {1} and end is {2}".format(res, start, end))
        return res