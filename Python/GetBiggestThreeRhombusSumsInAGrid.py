class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        ans = []
        
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                
                # by itself the cell is a rhombus, so we always want to add that to our ans
                ans.append(grid[i][j])
                
                # distance variable to store the distance from j to the both ends of rhombus
                distance = 1 
                # current sum
                expansionSum = grid[i][j]
                
                while(i + distance < rows and j - distance >= 0 and j + distance < cols):
                    # keep going down by dist which is increasing by 1 in every iteration 
                    ii = i + distance
                    
                    # keep going to the right by dist which is increasing by 1 in every iteration
                    jRight = j + distance
                    # keep going to the left by dist which is increasing by 1 in every iteration
                    jLeft = j - distance
                    
                    # add other left/right points to sum on the expansion phase
                    expansionSum += grid[ii][jRight] + grid[ii][jLeft]
                    
                    '''
                                                x <-------- grid[i][j]
                                               x x
                                              x   x <-------- grid[ii][jRight]
                      grid[ii][jLeft] -----> x     x
                                            x       x <-------------------- up till here is the expansion phase
                                             x     x <------------------- from here onward, the contraction phase
                                              x   x  
                                               x x
                                                x
                    
                    
                    but wait a minute, we need to consider all sub rhombuses under the above rhombus like:
                    
                                                y 
                                               y y
                                              y   y 
                                             x y y x
                                            x   y   x 
                                             x     x 
                                              x   x  
                                               x x
                                                x
                                
                    for example, the rhombus marked with 'y' needs to also be considered
                    so we need to do expansion followed by contraction immediately
                    
                    ie, expand up till 'y' and then immediately contract and complete rhombus
                    then expand up till the next side (size = 4) and immediately contract and complete rhombus
                    '''
                    
                    # enter into contraction phase
                    # sum of internal rhombus in the contraction phase
                    contractionSum = 0    
                    while True:
                        # move left pointer for column rightward
                        jLeft +=1
                        # move right pointer for column leftward
                        jRight -=1  
                        # move row pointer downward
                        ii +=1 
                        
                        if jLeft == cols or jRight == 0 or ii == rows:
                            break
                        
                        # found the bottom point of rhombus, ie, 4th side
                        # so add to contraction sum and append to answer
                        if jLeft == jRight: 
                            
                            # doesn't matter, jLeft or jRight are the same
                            contractionSum += grid[ii][jLeft]
                            
                            ans.append(expansionSum + contractionSum)
                            break
                        
                        # keep adding to the sum in the contraction phase
                        contractionSum += grid[ii][jLeft] + grid[ii][jRight]
                    
                    # increment dist by 1 to get next expansion phase sum for the next iteration
                    # which gets stored in 'expansionSum'
                    # expansion sum gets reset everytime the outer while loop is exhausted, ie,
                    # we have run out of rows/cols to expand into
                    '''
                        1st iteration
                                x
                               x x
                    
                        2nd iteration
                                x
                               x x
                              x   x
                        
                        3rd iteration
                                x
                               x x
                              x   x
                             x     x
                    '''
                    distance +=1
        
        # get only unique values
        ans = list(set(ans))
        # sort desc by sum
        ans.sort(reverse=True)
        # return top 3
        return ans[:3]