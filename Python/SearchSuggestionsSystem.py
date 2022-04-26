# https://leetcode.com/problems/search-suggestions-system/
class Trie():
    def __init__(self):
        self.isEnd = False
        self.children = dict()
    
    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
                
            cur = cur.children[c]
        cur.isEnd = True
    
    def startsWith(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return True
    
    def getWords(self, word):
        cur = self
        
        # this is being done to move in sorted order of keys in this function
        # alphabet just contains [a,b,c....z]
        alphabet = []
        for i in range(26):
            alphabet.append(chr(ord('a')+i))
        
        # keep going down the trie, till the word has been exhausted
        for c in word:
            cur = cur.children[c]
        
        res = []
        if cur.isEnd:
            res.append(word)
        
        def dfs(node, wordSoFar):
            if node == None or len(res) >=3:
                return
            
            if node.isEnd:
                res.append(wordSoFar)
            
            for c in alphabet:
                if c in node.children:
                    dfs(node.children[c], wordSoFar + c)
        
        # perform a dfs for each child with a "word" prefix
        # note that we're performing the dfs in sorted order of keys [a,b,c,d...z] so we can add 
        # the condition of early return on "res", ie, if len(res) >= 3, return early
        for c in alphabet:
            if c in cur.children and len(res) < 3:
                dfs(cur.children[c], word + c)
        
        # returns only up to 3 items sorted by lexographical order
        # since we placed this constraint in the dfs above
        return res
                
            
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = Trie()
        # add all product words to trie
        for p in products:
            t.insert(p)
        
        result = []
        lenw = len(searchWord)
        j = 1
        while j <= lenw:
            # form each substring of the word from 0 to j
            # mouse becomes --> ["m", "mo", "mou", "mous", "mouse"]
            search = searchWord[:j]
            if t.startsWith(search):
                result.append(t.getWords(search))
            else:
                result.append([])
                
            j +=1
            
        return result