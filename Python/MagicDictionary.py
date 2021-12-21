# https://leetcode.com/problems/implement-magic-dictionary/description/
'''

The basic idea here is very simple: we construct a dictionary, whose key is the length of the given words, and the value
 is a list containing the words with the same length specified in the key. And when we search a word (say word “hello”)
 in the magic dictionary, we only need to check those words in dic[len(“hellow”)], ( named candi in my code).

'''
class MagicDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.wordsdic = {}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for i in dict:
            self.wordsdic[len(i)] = self.wordsdic.get(len(i), []) + [i]

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for candi in self.wordsdic.get(len(word), []):
            countdiff = 0
            for j in range(len(word)):
                if candi[j] != word[j]:
                    countdiff += 1
            if countdiff == 1:
                return True
        return False