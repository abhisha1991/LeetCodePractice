# https://leetcode.com/problems/number-of-visible-people-in-a-queue
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n

        # stores max heights from right to left
        stack = []
        
        # go from right to left
        for i in range(n-1, -1, -1):
            h = heights[i]
            
            # if current height is greater than stack top
            # then ith person will overpower the heights of other shorter people in the stack
            # so pop shorter people from the right of the stack
            while stack and h > stack[-1]:
                stack.pop()
                # ith person can see those shorter people, so add 1 to for the ith person's res for every short
                # person who is popped from the stack
                res[i] +=1
            
            # if there are still elements in the stack
            # this means that there is at least someone to the right of the current person
            # who is equal to or taller than current person
            if stack:
                # we can see this taller person to our right, so increment 1 for the ith person
                res[i] +=1
            
            # add current person to stack
            stack.append(h)
        
        return res