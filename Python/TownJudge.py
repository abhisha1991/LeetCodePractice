# https://leetcode.com/problems/find-the-town-judge/submissions/
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        dic = {}
        # add all persons to the dictionary
        for i in range(1, N+1):
            dic[i] = []
            
        # add the trust relationships
        for i in trust:
            dic[i[0]].append(i[1])
        
        # sort the list based on the length of the values list
        s = sorted(dic, key=lambda x: self.func(x, dic))
        # the first element is the candidate who is the town judge since ideally his list length should be 0
        if len(dic[s[0]]) > 0:
            return -1
        
        # this is important, remove the town judge from dictionary, else the below will always return -1
        del dic[s[0]]
        for i in dic:
            # if the town judge is not in the trust list of any other person, return -1
            if s[0] not in dic[i]:
                return -1
        # return the town judge 
        return s[0]
    
    def func(self, x, dic):
        return len(dic[x])