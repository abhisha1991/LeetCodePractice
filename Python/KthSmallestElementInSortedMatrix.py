# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        maxrows = min(k, n)
        # this uses a heap because its kth smallest element that we need
        heap = []
        
        '''
        for the first column, add elements to the heap where max rows = min(k, n)
        why is max rows = min(k, n)?
            if k > n: then we can add all 'n' row elements initially (ie, add the 1st col)
            if k < n: then we don't need to add the whole first col, we can just add top k rows in the 1st col
        '''
        for r in range(maxrows):
            # note that we keep the row, col information along with element when pushing into heap
            # why? so that we can navigate what element to add next to heap
            # of course for this initial pass, since we're adding 1st col, thus, col=0
            heapq.heappush(heap, (matrix[r][0], r, 0))
        
        
        '''
        now we just need to keep decrementing k every time we pop from heap
        when k becomes 0, we would have found our kth smallest element - since we used a min heap
        
        but we also need to keep adding elements to the heap to keep getting the 
        smallest element in heap on top as we traverse through the matrix 
        
        now how do we traverse through the sorted matrix such that 
        we ensure we are always seeking smallest elements to add to our heap?
        
        imagine you have below matrix and k = 5, so far heap is 
                        1
                       / \
                      3   4
        
        imagine you just popped from heap ==> you get (1, r=0, c=0)
        so if we had to add next smallest element, we'd want to add 5, ie, matrix[r][c+1], now heap is
                        
                        3
                       / \
                      4   5
        
        notice how we were able to access the 1st row's next smallest element (5) - SAME ROW TRAVERSAL
        because we had added '1' in our initial heap construction
        
        
        now we pop again, we get (3, 1, 0), now we'd want to add next smallest, ie, 6, ie, matrix[r][c+1]
                        
                        4
                       / \
                      5   6
                      
        notice how we were able to access 2nd row's next smallest element (6) - ACROSS ROW TRAVERSAL  
        because we had added '3' in our initial heap construction 
        
        1 5 8  20
        3 6 9  21
        4 7 11 40
        
        this is the way in which we are able to traverse through multiple rows and along the same row as well!
        we naturally pick the smallest element along the same/diff row because the rows/cols are sorted (given)
        '''
        while k:
            element, r, c = heapq.heappop(heap)
            k -=1
            
            # notice we need to check c < n-1 and not c < n, because we need c+1 to be < n
            if c < n-1:
                heapq.heappush(heap, (matrix[r][c+1], r, c+1))
        
        return element