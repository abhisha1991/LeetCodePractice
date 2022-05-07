# https://leetcode.com/problems/shortest-word-distance-ii
from collections import defaultdict
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        wd = wordsDict
        self.dic = defaultdict(list)
        for i in range(len(wd)):
            self.dic[wd[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        
        # notice that w1 and w2 will be sorted already 
        # since we entered their entries for the same word in incrementing order
        w1 = self.dic[word1]
        w2 = self.dic[word2]

        i = 0 # ptr for w1
        j = 0 # ptr for w2
        minDiff = sys.maxsize
        
        while i < len(w1) and j < len(w2):
            diff = abs(w1[i] - w2[j])
            if diff < minDiff:
                minDiff = diff
            
            # imagine w1 = [2, 4, 10]
            # and     w2 = [6, 8, 9]
            '''
            iteration 1, compare 2 and 6, update minDiff = 4, increment i
            iteration 2, compare 4 and 6, update minDiff = 2, increment i
            iteration 3, compare 10 and 6, minDiff = 4 (worse than 2), increment j (since 6 < 10)
            iteration 4, compare 10 and 8, minDiff = 2 (no change), increment j (since 8 < 10)
            iteration 5, compare 10 and 9, minDiff = 1 (update minDiff), increment j (since 9 < 10)
            return minDiff since end of w2 has been reached!
            '''
            if w1[i] < w2[j]:
                i +=1
            else:
                j +=1
        return minDiff
    
            

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)