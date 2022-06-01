# https://leetcode.com/problems/guess-the-word
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

import random
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def pruneCandidates(word, matchCount):
            wl = list(self.candidates)
            self.candidates = []
            for w in wl:
                m = 0
                for i in range(len(w)):
                    if w[i] == word[i]:
                        m +=1
                if m == matchCount:
                    self.candidates.append(w)
        
        
        self.candidates = wordlist
        matches = 0
        for i in range(10):
            # break early if we have required number of matches, so as to not call api again
            if matches == 6:
                break
            idx = random.randint(0, len(self.candidates)-1)
            w = self.candidates[idx]
            matches = master.guess(w)
            # this part is important, we're pruning the candidates to keep the ones whose number of matches is the same 
            # with our current word, ie, candidate 'w'
            # why? because this helps us reduce the search space and guarantees that the remaining candidates have AT LEAST
            # 'x' number of matches against the secret word, so we're in essence using this word 'w' as our reference word
            if matches != 6:
                pruneCandidates(w, matches)