# https://www.youtube.com/watch?v=W4R4GqdTfGY
import itertools
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack = []
        
        def isChar(c):
            return c != ',' and c >= 'a' and c <= 'z'
        
        e = expression
        i = 0
        while i < len(e):
            # print(f"expression: {e}, processing element: {e[i]}, stack is {stack}")
            if e[i] in [',', '{']:
                stack.append(e[i])
                i +=1
                continue
            
            if isChar(e[i]):
                # add char as a list to stack
                stack.append([e[i]])

            if e[i] == '}':
                res = []
                while stack and stack[-1] != '{':
                    ele = stack.pop()
                    if type(ele) == list:
                        # concat all lists up till {
                        res += ele
                
                if stack and stack[-1] == '{':
                    stack.pop()
                
                stack.append(res)
            
            # array on top of another array calls for a cartesian cross product from bottom to top
            while len(stack) >=2 and type(stack[-1]) == list and type(stack[-2]) == list:
                top = stack.pop()
                bottom = stack.pop()
                # print(f"top is {top} and bottom is {bottom}")
                joined = set()
                combined = [bottom, top]
                for element in itertools.product(*combined):
                    # element is a tuple, so convert to string
                    joined.add(''.join(element))
                
                # append joined as a list, not set
                stack.append(list(joined))
            
            i+=1
        
        # at the end there is only 1 element in stack
        # need sorted result, need to set the 0th element since it may have duplicates
        return sorted(set(stack[0]))