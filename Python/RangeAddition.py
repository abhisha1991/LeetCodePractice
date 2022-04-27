# https://leetcode.com/problems/range-addition/
# https://leetcode.com/problems/range-addition/discuss/84225/Detailed-explanation-if-you-don't-understand-especially-%22put-negative-inc-at-endIndex%2B1%22
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0] * (length+1)
        '''
        consider length = 5 and updates having only single element = [[1,3,2]]

        this means we start from an array of 0s of length 5, ie, [0, 0, 0, 0, 0] and we need to finally reach an array where we increment
        start index of 1 to end index of 3 with value 2, ie, [0, 2, 2, 2, 0] 

        initialize an array of size = length+1, why? because we need to access index e+1 and we don't want to go out of bounds
        so we have arr = [0, 0, 0, 0, 0, 0]

        then mark index start as value 2 and index end+1 as value -2
        arr = [0, 2, 0, 0, -2, 0]

        then iterate through arr and do cumulative prefix sum
        arr = [0, 2 + (0), 0 + (2+0), 0 + (0+2+0), -2 + (0+0+2+0), 0 + (-2+0+0+2+0)]
        arr = [0, 2, 2, 2, 0, 0]

        this is the final result
        now we can see why we did increment 2 at start pos and decrement 2 at end+1 position

        since we do cumulative sum at the end, the increment of 2 carries over to every element beyond the start pos
        also, since we do cumsum at the end, the decrement of 2 neutralizes the effect of increment of 2 starting at pos end+1 (which is desired)

        why end+1? because we want the end pos to ALSO get increment of 2 as part of the cumulative sum

        for other updates, say update array now is [[1,3,2], [2,4,5]] -- we can apply the markers at start and end+1 for each update
        and then do one final cumulative sum. Since sum is commutative (a + (b+c)) = ((a+b) + c), we dont have to worry about this messing things up
        '''
        for u in updates:
            s = u[0]
            e = u[1]
            inc = u[2]
            
            arr[s] += inc
            arr[e+1] -= inc
        
        for i in range(len(arr)):
            if i == 0:
                continue
            else:
                arr[i] = arr[i-1] + arr[i]
        
        return arr[:length]