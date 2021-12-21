# https://leetcode.com/problems/validate-stack-sequences/
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """        
        auxstack = []
        idx = 0
        for p in pushed:
            # keep adding to aux stack till the top element of aux doesnt match popped
            auxstack.append(p)
            while len(auxstack) > 0 and auxstack[-1] == popped[idx]:
                # the moment top element of aux matches popped, 
                # then you can pop that element from aux as you've found match
                # obviously, increment index as you want to pop more elements
                auxstack = auxstack[0:len(auxstack)-1]
                idx +=1
        return len(auxstack) == 0
    
    
'''
pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
push 1, 1 != 4
push 2, 2 != 4
push 3, 3 != 4
push 4, 4 == 4, so pop off 4 from aux and incremenent idx
etc.

'''