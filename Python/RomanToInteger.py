# https://leetcode.com/problems/roman-to-integer/submissions/

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        lens = len(s)
        if lens == 0:
            return 0
        
        val = dict()
        val["M"] = 1000
        val["D"] = 500
        val["C"] = 100
        val["L"] = 50
        val["X"] = 10
        val["V"] = 5
        val["I"] = 1
        
        i = 0
        # note - use while and not for
        while i < lens:
            if i + 1 < lens and val[s[i]] < val[s[i+1]]:
                total += val[s[i+1]] - val[s[i]]
                # because we used up both i+1 and i, we move over 2 elements
                i +=2
            else:
                total += val[s[i]]
                i +=1
            
        return total

'''
Now, recall that each symbol adds its own value, except for when a smaller valued symbol is before a larger valued symbol. 
In those cases, instead of adding both symbols to the total, we need to subtract the large from the small, adding that instead.
Therefore, the simplest algorithm is to use a pointer to scan through the string, 
at each step deciding whether to add the current symbol and go forward 1 place, or add the difference of the next 2 symbols and go forward 2 places
'''
