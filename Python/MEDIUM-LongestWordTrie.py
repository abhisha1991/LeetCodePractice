# https://leetcode.com/problems/longest-word-in-dictionary/description/
class Solution(object):
    def longestWord(self, words):
        words.sort()
        words_set, longest_word = set(['']), ''
        for word in words:
            if word[:-1] in words_set:
                words_set.add(word)
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word


s = Solution()
s.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])