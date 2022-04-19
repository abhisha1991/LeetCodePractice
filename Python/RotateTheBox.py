# https://leetcode.com/problems/rotating-the-box/
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows = len(box)
        cols = len(box[0])
        
        # define consts as shown in question
        stone = '#'
        air = '.'
        block = '*'
        
        # do the rotation, notice the rotation is clockwise so look at the inner for loop
        box = [[box[i][j] for i in range(rows-1,-1,-1)] for j in range(cols)]
        # recompute rows and cols
        rows = len(box)
        cols = len(box[0])
        
        def getcol(j):
            assert(j < cols)
            i = 0
            res = []
            while i < rows:
                res.append(box[i][j])
                i +=1
            return res
        
        def stoneSort(col):
            lencol = len(col)
            if lencol <= 1:
                return col
            
            # only stones have to move
            # if no stone is present, return as is
            if stone not in col:
                return col
            
            if block not in col:
                # sort between stone and air and return
                i = 0
                j = lencol-1
                while i <= j:
                    # find first stone from left
                    if col[i] != stone:
                        i+=1
                        continue
                    
                    # find first air from right
                    if col[j] != air:
                        j -=1
                        continue
                    
                    # swap stone and air
                    tmp = col[i]
                    col[i] = col[j]
                    col[j] = tmp
                    i +=1
                    j -=1
                    
                return col
            
            # there is a block present
            idx = col.index(block)
            # break array and sort each individual array and return concated result
            return stoneSort(col[0:idx]) + [block] + stoneSort(col[idx+1:])
        
        for j in range(cols):
            col = getcol(j)
            sortCol = stoneSort(col)
            i = 0
            while i < rows:
                box[i][j] = sortCol[i]
                i +=1
        
        return box