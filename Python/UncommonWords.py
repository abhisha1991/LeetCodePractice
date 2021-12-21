class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        dic = dict()
        for i in A.split(' '):
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] +=1
        
        for i in B.split(' '):
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] +=1
        
        res = []
        for i in dic:
            if dic[i] == 1:
                res.append(i)
        return res