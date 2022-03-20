# https://leetcode.com/problems/implement-trie-ii-prefix-tree/
class Trie:

    def __init__(self):
        self.isWordEnd = False
        self.countpf = 0 # count prefix
        self.countew = 0 # count end of word
        self.children = dict()

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
            # keep a count of instances of when we have passed through
            # that character path in the trie
            cur.countpf +=1
            
        cur.isWordEnd = True
        # end of word counter is only updated once
        # as opposed to countpf
        cur.countew +=1

    def countWordsEqualTo(self, word: str) -> int:
        cur = self
        for c in word:
            if c not in cur.children:
                # return 0 if word not found
                return 0
            # keep moving down the trie
            cur = cur.children[c]
        
        if cur.isWordEnd:
            return cur.countew
        return 0
            
    def countWordsStartingWith(self, prefix: str) -> int:
        cur = self
        for c in prefix:
            if c not in cur.children:
                # return 0 if prefix char match not found
                return 0
            # keep moving down the trie
            cur = cur.children[c]
        
        return cur.countpf
            
    def erase(self, word: str) -> None:
        cur = self
        # note that we are guaranteed to have word exist before we call erase
        # so we dont have to worry about counts (pf or ew) going negative
        for c in word:
            if c not in cur.children:
                # cannot erase a word not inserted in trie
                return
            
            # keep moving down the trie and decrement a count
            cur = cur.children[c]
            cur.countpf -=1
        
        # reduce its count of end of word once erased, 
        # this will naturally handle the case where we advertise zero counts for a word
        # notice we don't actually delete any nodes from the trie, we just update its end of word count
        
        # there could be multiple instances of a word, ie, insert "apple" 10 times
        # in such a case, if we erase once, then end of word of apple, ie, "e" will have count=9
        # this will also be handled by the counter
        if cur.isWordEnd:
            cur.countew -= 1
            
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)