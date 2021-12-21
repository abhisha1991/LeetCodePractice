# https://leetcode.com/problems/daily-temperatures/

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = [0] * len(T)
        for i, t in enumerate(T):
            while len(stack) > 0 and T[stack[-1]] < t:
                topidx = stack.pop()
                ans[topidx] = i - topidx
            stack.append(i)
            
        return ans

'''
input:[73,74,75,71,69,72,76,73]
here, stack holds the indexes of the elements who dont have an answer
't' is the current element being evaluated to be appended into the stack
if 't' is larger than the top stack element T[stack[-1]], then that index element, stack[-1] - has found someone who is greater temp than itself.
So the difference between the index of the 'greater temp' and our own temp (stack[-1]) is what we want to record

trace this out to understand further

'''