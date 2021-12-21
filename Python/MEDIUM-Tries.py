from collections import defaultdict
# https://leetcode.com/problems/implement-trie-prefix-tree/description/


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.endofword = False
        self.dic = defaultdict(Trie)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        self.inserthelper(word, self)
        print("inserted", word)

    def inserthelper(self, word, t):
        if len(word) == 0:
            return

        first = word[0]
        if len(word) == 1:
            if t.dic[first] == None:
                t.dic[first] = Trie()

            t.dic[first].endofword = True
            return

        rest = word[1:]
        if t.dic[first] == None:
            t.dic[first] = Trie()

        self.inserthelper(rest, t.dic[first])

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return self.searchhelper(word, self)

    def searchhelper(self, word, t):
        if len(word) == 0:
            return True

        first = word[0]
        if len(word) == 1:
            if first not in t.dic.keys():
                return False
            if t.dic[first].endofword == False:
                return False

        rest = word[1:]

        if first not in t.dic.keys():
            return False

        return self.searchhelper(rest, t.dic[first])

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.startswithhelper(prefix, self)

    def startswithhelper(self, prefix, t):
        if len(prefix) == 0:
            return True

        first = prefix[0]

        if first not in t.dic.keys():
            return False

        rest = prefix[1:]
        return self.startswithhelper(rest, t.dic[first])

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)