# https://leetcode.com/problems/sort-characters-by-frequency/submissions/
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] +=1
        # sort by decreasomg value's frequency
        tmp = sorted(dic, key=dic.get, reverse = True)
        res = []
        for key in tmp:
            res.append(key * dic[key]) 
        return "".join([i for i in res])