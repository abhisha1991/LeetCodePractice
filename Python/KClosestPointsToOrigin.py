from collections import defaultdict

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dic = defaultdict(list)
        for i in points:
            dic[(i[0] * i[0]) + (i[1] * i[1])].append(i)
        
        i = 0
        res = []
        for key in sorted(dic.keys()):
            for j in range(len(dic[key])):
                if i >= K:
                    return res
                res.append(dic[key][j])
                i +=1
            
        return res