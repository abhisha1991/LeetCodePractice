# https://leetcode.com/problems/reorder-data-in-log-files/
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        digit = []
        
        for l in logs:
            log = l.split(' ')
            first = log[0]
            second = log[1]
            notFirst = " ".join(log[1:])
            
            if second.isdigit():
                digit.append(l)
            else:
                letter.append([first, notFirst])
                
        letter = sorted(letter, key=lambda x: (x[1], x[0]))
        letter = [x[0] + " " + x[1] for x in letter]
        
        return letter + digit