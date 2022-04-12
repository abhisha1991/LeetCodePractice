# https://leetcode.com/problems/top-k-frequent-words/
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = dict()
        for w in words:
            if w in dic:
                dic[w] +=1
            else:
                dic[w] = 1
        
        arr = [(v, k) for k,v in dic.items()]
        arr = sorted(arr, key=lambda x: (-x[0],x[1]))
        arr = arr[:k]
        return [v[1] for v in arr]