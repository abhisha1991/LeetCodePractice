# https://leetcode.com/problems/brace-expansion
import itertools
class Solution:
    def expand(self, s: str) -> List[str]:
        dic = dict()
        group = 0
        
        i = 0
        parse = False
        while i < len(s):
            if s[i] == '{':
                parse = True
                i +=1
                continue
                
            # parse everything from { to } -- like {a,b} -- we want to capture ab without commas
            if parse:
                key = ''
                while i < len(s) and s[i] != '}':
                    if s[i] == ',':
                        i +=1
                        continue
                    else:
                        key += s[i]
                        i +=1
                
                if s[i] == '}':
                    parse = False
                    dic[group] = list(key)
                    group +=1
                    i +=1
                    continue
            
            # consider a case like "xy{a,b}c{d,e}f" -- we want to capture words like "xy", "c" and "f"
            if (i == 0 and s[i] != '{') or (i > 0 and s[i-1] == '}'):
                key = ''
                while i < len(s) and s[i] != "{":
                    key += s[i]
                    i +=1
                
                # this is important, we don't want to make a single char list in this case, since "xy" (say)
                # needs to always come together in output, not as either 'x' or 'y' - as was the case with {a,b}
                dic[group] = [key]
                group +=1
        
        ans = set()
        '''
        at this point, for input say "xy{a,b}c{d,e}f"
        we have dic as 
        dic[0] = ['xy']
        dic[1] = ['a', 'b']
        dic[2] = ['c']
        dic[3] = ['d', 'e']
        dic[4] = ['f']
        note that the key order is important because we can form a string like xyacdf but NOT axydcf
        '''
        
        # we need to now create a cartesian product between the lists
        combined = []
        # note the order is important in which we're adding the lists
        for i in range(len(dic)):
            combined.append(dic[i])
            
        for element in itertools.product(*combined):
            # element is a tuple, so convert to string
            ans.add(''.join(element))
        
        return sorted(list(ans))