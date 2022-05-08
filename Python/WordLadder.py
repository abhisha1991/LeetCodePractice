# https://leetcode.com/problems/word-ladder/description/
from collections import defaultdict
class Solution:
    # time and space complexity that makes this acceptible on leetcode is o(m*m*n) 
    # where n = len(wordList), which can be 5000 and m = len(word) in wordList, which is small (max 10)
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        dicPattern2Words = defaultdict(list)
        dicWord2Patterns = defaultdict(list)
        
        for i in range(len(wordList)):
            cur = wordList[i]
            for j in range(len(cur)):
                # so a word like hot becomes -- '*ot', 'h*t', 'ho*'
                # and we store a mapping from word to pattern and pattern to word
                pattern = cur[:j] + '*' + cur[j+1:]
                
                if pattern not in dicPattern2Words:
                    dicPattern2Words[pattern] = [cur]
                else:
                    dicPattern2Words[pattern].append(cur)
                
                if cur not in dicWord2Patterns:
                    dicWord2Patterns[cur] = [pattern]
                else:
                    dicWord2Patterns[cur].append(pattern)
                
        q = [(beginWord,1)]
        visited = set()
        
        # bfs
        while q:
            first = q.pop(0)
            word = first[0]
            level = first[1]
            visited.add(word)
            
            if word == endWord:
                return level
            
            patterns = dicWord2Patterns[word]
            for p in patterns:
                nbors = dicPattern2Words[p]
                q.extend([(n, level + 1) for n in nbors if n not in visited])
                
        return 0