# https://leetcode.com/problems/longest-string-chain 
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if len(words) < 2:
            return len(words)
        
        # doing this for o(1) access for any word
        # to check if its in the word list or not
        # else it would be o(n) access if we use the word list
        setw = dict()
        for w in words:
            setw[w] = 0
        
        # key is word in word list, value is longest word chain length
        # this assumes that key was the final ending word
        # so value is how many hops does it take to get from the smallest length word (say 1 letter word) to this word
        # for example, consider ["a", "b", "bc", "abc"]
        # if current word is "abc", it takes 3 hops to get to abc, ie, "b" --> "bc" --> "abc"
        res = dict()
        
        # top down approach
        def dfs(word):
            if word not in setw:
                return 0
            else:
                if len(word) == 1:
                    return 1
            
            if word in res.keys():
                return res[word]
            
            # stores number of steps it takes to get to this current word
            # assuming this current word is the "end word"
            arr = []
            for i in range(len(word)+1):
                # create all new words removing 1 char from original word
                newWord = word[0:i] + word[i+1:]
                
                # avoid going into infinite loop
                if newWord == word:
                    continue
                
                if newWord not in res.keys():
                    arr.append(dfs(newWord))
                else:
                    arr.append(res[newWord])
            
            # number of steps it would take would be 1 + max of 
            # (all words that are 1 char less than this original word)
            res[word] = 1+max(arr)
            return res[word]
        
        # run dfs over all words in word list
        for w in words:
            dfs(w)
        
        # return max value, ie, max number of steps it takes to get to a word in the word list
        maxv = 0
        for k,v in res.items():
            if v > maxv:
                maxv = v
        return maxv