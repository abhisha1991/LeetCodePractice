# https://leetcode.com/problems/reaching-points/
class Solution:
    # this is the optimal solution: https://www.youtube.com/watch?v=tPr5Uae6Drc
    '''
            source is 1,9 and target is 100,9
            
                                    1,9
                                    /  \
                                 10,9   1,10
                                 / \       \
                             19,9   10,19    ....
                               / \       \
                           28,9  19,28    ....
                            /\        \
                        37,9  28,37   ....
                         /
                      46,9      not adding to this sub tree anymore...
                      /
                    55,9
                    /
                  64,9
                  /
                 73,9
                  /
                 82,9
                /   \
              91,9  82,91
              /  \     
         100,9   91,100
         
         so instead of going backwards one step at a time from target to source
         we use modulo and skip all of the steps -- for example, if we did 100 % 9 = 1, we can get to 1,9 immediately
         
         let's use a less extreme example and see an edge case
         source: 3,3 and target: 21,9
         
                                    3,3
                                    / \
                                 6,3   3,6
                                 /     /  \
                                     9,6  3,9
                                          /  \
                                        3,12  12,9
                                        ...    /  \
                                            21,9   12,21

         imagine we're at 21,9 -- now 21 > 9, so if we do 21 % 9 = 3, so we can go to 3,9 (ie, we skipped 12,9)
         [edge case] do this for 3,9 now -- now 9 > 3, so 9 % 3 = 0, this takes us to 3,0 (here we overshot 3,3)
         we could have reached 3,3 -- but instead it took us straight to 3,0 -- how to solve this?
         
         take another example, where this can be made clear: say you're going from 2,3 to 2,11
                                            2,3
                                            /  \
                                           5,3  2,5
                                                /  \
                                             7,5    2,7
                                                    /  \
                                                       2,9
                                                         \
                                                         2,11
                                                         
        now 11 > 2 => 11 % 2 = 1 ==> we will again overshoot and reach 2,1 instead of 2,3 (similar to the above problem)
        
        instead, we can see if the x values in source and target are the same, ie, 2, then do targetY - sourceY and see if that's
        divisible by the x value, here at 2,11 (target) and 2,3 (source), x val is the same and less than 11-3 = 8
        now 8 % 2 = 0, this means that we can reach 2,3 from 2,11
        
        why? because we're just interested in using the x value, 2, to decrement the target y (11) to source y (3)
        we need to just decrement the target 11 by 8 to reach 3, this diff of 8 can be found by 11-3
    '''
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            
            if tx <= ty:
                # if source and dest x values are same, check if diff is div by tx
                if tx == sx:
                    if (ty - sy) % tx == 0:
                        return True
                # else take the bigger num ty and modulo it by smaller num tx
                ty = ty % tx
            else:
                # if source and dest y values are same, check if diff is div by ty
                if ty == sy:
                    if (tx - sx) % ty == 0:
                        return True
                # else take the bigger num tx and modulo it by smaller num ty
                tx = tx % ty
        
        return False
    
    
    # this approach is fine, but errors, since max recursion depth exceeds
    # problem is that we're starting at source points and going to dest points
    # so as a result, we're having to go down 2 branches at every level
    # let's do the opposite instead, lets go from target to source by subtraction
    # how does this help? from a target, there is only 1 path to a source/parent -- so lesser computation
    # (since points must be positive) - ie, subtract the smaller of the 2 at every step
    def reachingPointsInefficient(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        search = dict()
        def helper(sx, sy):
            if sx > tx or sy > ty:
                return
            
            if (sx,sy) in search:
                return
            
            search[(sx,sy)] = True
            
            helper(sx + sy, sy)
            helper(sx, sy + sx)
            
        helper(sx, sy)
        
        if (tx,ty) in search:
            return True
        return False
    
    # this is better, since we're going from target to source, but time limit still exceeds
    def reachingPoints2(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if sx == tx and sy == ty: 
                return True
            if tx > ty:
                tx -= ty
            else:
                ty -= tx
        return False