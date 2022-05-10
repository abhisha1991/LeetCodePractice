# https://leetcode.com/problems/verifying-an-alien-dictionary
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = dict()
        for i in range(len(order)):
            dic[order[i]] = i
        
        # introduce a new char in the order dictionary, that represents blank space
        dic['#'] = -1
        
        # get the max len of all words
        maxlen = max([len(w) for w in words])
        
        # if there are 2 uneven sized words, make them even sized
        # say there's ['ab', 'abc'], then this processing gives us ['ab#', 'abc']
        # here the '#' is representing a blank space
        for i in range(len(words)):
            lw = len(words[i])
            if lw < maxlen:
                diff = maxlen - lw 
                words[i] += '#' * diff
        
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                w1 = words[i]
                w2 = words[i+1]
                
                # find first char that is mismatching in the 2 words
                # this differing char must be such that the order of the first word
                # is lesser than the order of the 2nd word (in order to keep lex order)
                if w1[j] != w2[j]:
                    if dic[w1[j]] > dic[w2[j]]:
                        return False
                    break
        return True