# https://leetcode.com/problems/word-break/description/
class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)  # dp[i] means s[:i] can be segmented into words in the wordDicts
        dp[0] = True # empty string is always true
        for i in range(len(s)):
            print("dp[i]", i, dp[i])
            for j in range(i, len(s)):
                print("s[i: j + 1]", i, j, s[i: j + 1])
                # if s[:i+1] is true, ie - dp[i] is true, ie - the first part of the string is true from 0 to i
                # and if the second part of the string s[i:j+1] is in wordDict, from i to j+1
                # here we are testing j from i to len(string),
                # ie - testing entire word eventually, s[i:i+1] and s[i:len(s)]
                if dp[i] and s[i: j + 1] in wordDict:
                    # this means that dp[i] is True and s[i:j+1] is in wordDict
                    # this means that s[:i] is in word dict and s[i:j+1] is in word dict
                    # this means that s[:j+1] is in word dict, ie - first j char in word dict
                    # we're doing j+1 here because 0th index represents blank char, first char of 's' starts from 1
                    dp[j + 1] = True
                    print("dp[j + 1] was made True", j+1)
        print(dp)
        return dp[-1]

s = Solution()
# s.wordBreak("cars", ["car", "ca", "rs"])
s.wordBreak("goalspecial", ["go","goal","goals","special"])


# much easier to understand, however, this is not optimal as this re-calculates the same result several times
class Solution2(object):
    def wordBreak(self, s, wordDict):
        if len(s) is 0:
            return True

        i = 1
        while i <= len(s):
            if s[:i] in wordDict:
                res = self.wordBreak(s[i:], wordDict)
                if res:
                    return res
            i += 1
        return False