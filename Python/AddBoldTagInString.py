# https://leetcode.com/problems/add-bold-tag-in-string
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        intervals = []
        for w in words:
            if w in s:
                count = s.count(w)
                idx = 0
                # finds the starting index of word 'w' in string 's'
                idx = s.find(w)

                # we need to get all repeating occurrences of 'w' in 's'
                # thus we need to capture all occurrence intervals of w
                while count >= 0 and idx != -1:
                    intervals.append([idx, idx + len(w)])
                    # start finding word 'w' from start pos idx+1
                    # idx returns -1 if 'w' is not found in 's'
                    idx = s.find(w, idx+1)
                    count -=1

        intervals.sort()
        merged = []
        # do merge intervals
        while intervals:
            s1, e1 = intervals.pop(0)
            if not merged:
                merged.append([s1, e1])
            else:
                s2 = merged[-1][0]
                e2 = merged[-1][1]
                # if 2 intervals overlap
                if (s1 >= s2 and s1 <= e2) or (e1 >= s2 and e1 <= e2):
                    # then merge
                    s2, e2 = merged.pop()
                    merged.append([min(s1, s2), max(e1, e2)])
                else:
                    # 2 intervals don't overlap, so we can append the incoming interval
                    merged.append([s1, e1])
        
        # create result arr
        arr = []
        # if there were no merged intervals, we can return string as is as there is no place to put the bold tag
        if not merged:
            return s
        
        # we need to insert the bold tag at the indices provided in these merged intervals
        cur = merged.pop(0)
        for i in range(len(s)):
            if i == cur[0]:
                arr.append('<b>')
                arr.append(s[i])
            
            elif i == cur[1]:
                arr.append('</b>')
                arr.append(s[i])
                # pick the next interval and assign as cur
                if merged:
                    cur = merged.pop(0)
            
            else:
                arr.append(s[i])
        
        # consider s = "abcxyz123", words = ["abc","123"]
        # length of s is 9
        # here merged will be [[0,3], [6,9]]
        # so we need to insert the last closing bold tag at pos 9, ie, end of string
        if cur[1] == len(s):
            arr.append('</b>')
            
        return ''.join(arr)