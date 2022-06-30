# https://leetcode.com/problems/remove-invalid-parentheses
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # tracks the MIN number of open and close brackets we can remove to get a valid string
        # a valid string is defined by equal number of closing and opening brackets
        leftRemovalCapacity = 0
        rightRemovalCapacity = 0
        
        for c in s:
            if c not in [')', '(']:
                continue
            
            if c == '(':
                leftRemovalCapacity +=1
            
            # when we encounter a right paranthesis, only if left removal capacity was 0 can we remove a right bracket
            # so add +1 to right removal capacity
            # if left removal capacity > 0, then we don't need to add to right removal capacity, we can just subtract left capacity
            # why? consider if you had (())
            # then you would have left removal capacity = 2, which would get counter balanced by the right brackets
            # so instead of adding to right capacity, just subtract from left capacity
            
            # but consider if you had (())) or )(()) => then there would be one extra right bracket which can be removed
            # so we need to increment right capacity
            elif c == ')':
                if leftRemovalCapacity == 0:
                    rightRemovalCapacity +=1
                else:
                    leftRemovalCapacity -=1
        
        
        self.res = set()
        self.string = s
        
        def dfs(idx, curLeftCount, curRightCount, leftCapacity, rightCapacity, stringSoFar):
            # if we've reached end of string, then check if we have a valid parantheses result and if so, add it to res
            if idx == len(self.string):
                # conditions for a valid parantheses string are if open bracket count == closed bracket count
                # AND if there is no removal capacity in open and close bracket
                if curLeftCount == curRightCount and leftCapacity == 0 and rightCapacity == 0:
                    self.res.add(stringSoFar)
                return
            
            # get current character from string
            cur = self.string[idx]
            
            # can be a regular char, in which case we have to add it to string builder
            if cur not in [')', '(']:
                dfs(idx + 1, curLeftCount, curRightCount, leftCapacity, rightCapacity, stringSoFar + cur)
            
            # now we know cur is a paranthesis
            # we can either retain or ignore the paranthesis - both open and closed
            
            elif cur == '(':
                if leftCapacity > 0:
                    # consider ignoring open paranthesis from string builder, 
                    # ie, remove open paranthesis
                    dfs(idx + 1, curLeftCount, curRightCount, leftCapacity-1, rightCapacity, stringSoFar)
                
                # consider adding open paranthesis to string builder
                # ie, retain the open paranthesis
                dfs(idx + 1, curLeftCount + 1, curRightCount, leftCapacity, rightCapacity, stringSoFar + cur)
            
            elif cur == ')':
                if rightCapacity > 0:
                    # consider ignoring closed paranthesis from string builder, 
                    # ie, remove closed paranthesis
                    dfs(idx + 1, curLeftCount, curRightCount, leftCapacity, rightCapacity-1, stringSoFar)
                
                # this condition is key in the case of the closed paranthesis, we can retain the closed paranthesis
                # IFF AND ONLY IFF the open paranthesis count is > closed paranthesis count so far
                # if open paranthesis count was less than closed, example, ( ( ) ) ')' ( )  ==> then we can't add the closed 
                # paranthesis that is marked in quotes as we'd be guaranteed to get an invalid string
                if curLeftCount > curRightCount:
                    # consider adding closed paranthesis to string builder
                    # ie, retain the closed paranthesis
                    dfs(idx + 1, curLeftCount, curRightCount + 1, leftCapacity, rightCapacity, stringSoFar + cur)
        
        dfs(0, 0, 0, leftRemovalCapacity, rightRemovalCapacity, "")
        return list(self.res)