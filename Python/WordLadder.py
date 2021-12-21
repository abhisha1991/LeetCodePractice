# https://www.geeksforgeeks.org/word-ladder-length-of-shortest-chain-to-reach-a-target-word/
# https://leetcode.com/problems/word-ladder/description/
# this solution is close to correct, however, it doesnt give the optimal number of hops
class Solution(object):
    def __init__(self):
        self.count = 0
        self.nbors = []
        self.visited = []

    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        if self.ladderFind(beginWord, endWord, wordList):
            return self.count
        return 0

    def ladderFind(self, beginWord, endWord, wordList):
        self.nbors.append(beginWord)

        while len(self.nbors) > 0:
            i = self.nbors[0]
            self.nbors = self.nbors[1:]
            if i in self.visited:
                continue

            self.visited.append(i)

            if i == endWord:
                return True

            wordList = set(x for x in wordList if x != i)
            self.nbors.extend(self.getAllNbors(i, wordList))

        return False

    def getAllNbors(self, word, wordList):
        nbors = []
        for i in wordList:
            if self.isEditDistOne(word, i):
                nbors.append(i)
        return nbors

    def isEditDistOne(self, a, b):
        # note - a and b have the same length in this problem
        m = len(a)
        i = 0
        j = 0
        count = 0
        while i < m and j < m:
            if a[i] == b[j]:
                i +=1
                j +=1
                continue
            else:
                if count == 1:
                    return False
                count += 1
                i +=1
                j +=1

        return count == 1

s = Solution()
print(s.ladderLength("hit", "cog", ["hot", "dog", "dot", "lot", "log", "cog"]))