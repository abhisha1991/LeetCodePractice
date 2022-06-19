# https://leetcode.com/problems/ipo
import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # min heap for capital
        pqCapitalMn = []
        # max heap for profit
        pqProfitMx = []
        
        # ingest all items into min heap
        # minimum cost will bubble to the top
        for i in range(len(capital)):
            c = capital[i]
            p = profits[i]
            
            heapq.heappush(pqCapitalMn, (c, p))
        
        
        # count is project count and should be < k
        count = 0
        while count < k:
            # capital is a minheap so top item will be min cost (capital) item
            # so while we have options such that the min capital item is less than our available capital 'w'
            # keep popping from that heap and putting onto the profit heap
            while pqCapitalMn and w >= pqCapitalMn[0][0]:
                c, p = heapq.heappop(pqCapitalMn)
                # profit heap is a max heap, so we insert -p
                heapq.heappush(pqProfitMx, (-p, c))
            
            if pqProfitMx:
                # get the max profit item from the max heap
                pp, cc = heapq.heappop(pqProfitMx)
                # profit is negative, so we need to take -ve of that to get +ve value
                pp = -1 * pp

                # add profits to capital and increment project count 
                w += pp
                count +=1
                
            else:
                '''
                k = 1
                w = 0
                profits = [1,2,3]
                capital = [1,1,2]
                
                imagine if all capital values have higher value than available capital 'w' 
                then we just break and return w
                '''
                break
        
        return w