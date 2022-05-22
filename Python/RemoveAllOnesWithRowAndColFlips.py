# https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips
class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        if not grid:
            return False
        
        # get first row and mirror image of first row
        # for example, if first row is 101, then mirror is 010
        row = grid[0]
        rowMirror = [1-val for val in grid[0]]
        
        '''
        below logic is simple, it is iterating row by row from 2nd row onward
        and checking if that current row matches either 'row' or 'rowMirror'
        in the left example, every row matches one of those 2 patterns
        in the right example, 2nd row doesn't match any of those 2 patterns

            1 0 1                 1 0 1
            0 1 0 ==> true        0 1 1 ==> false
            1 0 1                 0 1 0

        why is it important to match those patterns?
        because, if they match any of those patterns, then we can eventually get them to get to a state like
        1 0 1     0 1 0
        1 0 1 OR  0 1 0
        1 0 1     0 1 0

        once we have this stage, all col values are same, so we can flip each col to become 0
        example:

        0 0 0
        0 0 0
        0 0 0
        flip 1st and 3rd col

        '''
        for i in range(1, len(grid)):
            if grid[i] != row and grid[i] != rowMirror:
                return False
        return True