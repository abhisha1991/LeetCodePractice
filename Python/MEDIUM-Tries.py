# https://www.youtube.com/watch?v=asbcE9mZz_U
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
class Trie:
    def __init__(self):
        self.isWordEnd = False
        self.children = dict()

    def insert(self, word: str) -> None:
        # start at root
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            # remember to move down the trie
            cur = cur.children[c]
        # remember to mark word end after going through all characters
        cur.isWordEnd = True

    def search(self, word: str) -> bool:
        # start at root
        cur = self
        for c in word:
            # if at any point you're unable to find the key of the word in the tree
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        # the word is completely found IFF it is an end of word in the trie
        return cur.isWordEnd

    # similar to search, with a minor tweak
    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        # doesn't matter if its end of word or not, always return true
        # complete word is also a prefix
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)