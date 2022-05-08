# https://leetcode.com/problems/word-ladder-ii/
from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList.append(beginWord)
        
        dicPattern2Words = defaultdict(list)
        dicWord2Patterns = defaultdict(list)
        
        for i in range(len(wordList)):
            cur = wordList[i]
            for j in range(len(cur)):
                pattern = cur[:j] + '*' + cur[j+1:]
                if pattern not in dicPattern2Words:
                    dicPattern2Words[pattern] = [cur]
                else:
                    dicPattern2Words[pattern].append(cur)
                
                if cur not in dicWord2Patterns:
                    dicWord2Patterns[cur] = [pattern]
                else:
                    dicWord2Patterns[cur].append(pattern)
        
        q = deque()
        # q contains word and path so far as 2 inputs of an object
        q.append((beginWord, [beginWord]))
        visited = set()
        
        # the list of paths from begin to end
        # may contain all potential paths, and may contain the same path duplicates too!
        # will need to dedupe/filter as we return the result
        resPaths = []
        
        # length of minpath, this is a gating condition check to add to resPaths
        minPath = sys.maxsize
        
        #bfs
        while q:
            first = q.popleft()
            word = first[0]
            path = first[1]
            visited.add(word)
            
            if word == endWord:
                resPaths.append(path)
                
            patterns = dicWord2Patterns[word]
            for p in patterns:
                nbors = dicPattern2Words[p]
                q.extend([(n, path + [n]) for n in nbors if n not in visited])
        
        # post processing of resPaths to dedupe and only return min length paths
        if resPaths:
            for p in resPaths:
                minPath = min(len(p), minPath)
            
            result = []
            for p in resPaths:
                if len(p) == minPath and p not in result:
                    result.append(p)
                    
            return result
        
        return []