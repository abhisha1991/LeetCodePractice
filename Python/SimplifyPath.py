# https://leetcode.com/problems/simplify-path/
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        parts = path.split('/')
        for p in parts:
            # its only in this case where we need to move one directory up
            # ie, we need to pop from the stack
            if p == '..':
                if stack:
                    stack.pop()
            
            # the case of empty string will occur when we have something like a//b, 
            # when we split by '/', we get ['a', '', 'b']
            # when we have a period, like a/./b ==> ['a', '.', 'b']
            # we are just saying that we want to stay on the present directory, so its a no-op 
            elif p == '' or p == '.':
                continue
            
            else:
                # if we have a legit folder name like 'a' or 'b'
                # then insert that into stack
                stack.append(p)
        
        # remember to add '/' in the front of the string as all paths must begin with it
        # all elements of the stack, which are now directory names, must be joined with '/'
        return '/' + '/'.join(stack)
