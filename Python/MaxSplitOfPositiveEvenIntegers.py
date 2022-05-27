# https://leetcode.com/problems/maximum-split-of-positive-even-integers
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
        
        ans = []
        i = 2
        '''
                28
               /  \
              2    26
                  /  \ 
                 4    22
                     /  \
                    6   16
                       /  \
                      8 +  8 = 16 (this is what the last step is doing: ans[-1] = ans[-1] + finalSum)
                          /
                         10 (terminal condition i > finalSum, ie, 10 > 8)
                           
        we are guaranteed to pick the longest sequence of even integers because we are starting from the smallest
        2, 4, 6, 8 ....
        
        when we cannot add any more elements, we just add whatever is the remainder in the 'finalSum' to the last element
        '''
        
        while i <= finalSum:
            ans.append(i)
            finalSum -= i
            i +=2
        
        # we are adding even number, ie, ans[-1] to another even number, ie, remainder finalSum
        # so this will also be even
        ans[-1] = ans[-1] + finalSum
        return ans