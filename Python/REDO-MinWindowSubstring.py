# https://leetcode.com/problems/minimum-window-substring/description/
from collections import defaultdict

# this is a great problem
'''
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Here we are not interested in the freq of occurrence of char of s string, but rather we want freq of occurrence of t string.

ie - we want to have a dic such that initially
dic[A] = 1
dic[B] = 1
dic[C] = 1 
walk through this example on paper, if unclear

'''
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        slen = len(s)
        dic = defaultdict(int)
        for i in s:
            # add a frequency of 0 for each char in s
            dic[i] = 0

        for i in t:
            # if the char belonging to 't' doesnt already belong in dic
            # this means that there is atleast 1 char in 't' not in 's' => t is not a subset of s
            # hence, return empty window
            if i not in dic.keys():
                return ""
            else:
                dic[i] += 1

        # up till here dic has freq of 't'
        '''
        positive values in dic's values implies that we haven't found all char of 't' in the window we are observing
        dic's value being 0 for a given key implies that we have found that key EXACTLY once in the window
        dic's value being negative for a given key implies we have found that key more than once in window
        '''
        answer = None
        # the minwin is the min window size, initially set to the entire string, ie - 't' is a subset in all of 's'
        minwin = slen + 1
        left = 0
        right = 0
        while right <= slen:
            # if we have found all characters of 't' atleast once in sliding window
            if all(map(lambda x: True if x <= 0 else False, dic.values())):
                # we have a potential window that could be smaller than existing window of len minwin
                if minwin > right - left:
                    minwin = right - left
                    # if we have a smaller window, set a new answer
                    answer = s[left:right]

                # after getting a potential sliding window of min length, we look for a smaller window ahead
                # not to rest on our laurels, we move the window ahead from the left
                # and make the dictionary such that we are
                # missing a character which we hope to find in a new window ahead
                if s[left] in dic.keys():
                    dic[s[left]] += 1
                # we check if we can move the window ahead by advancing left to find a smaller window
                left += 1
            else:
                # we have not found a window, there is atleast 1 character of 't'
                # which is missing to appear in the window
                if right == slen:
                    break
                # if current right character is in dic, then we should decrease its value
                # as the window has satisfied a char from 't'. This may give us a new sliding window to check later
                if s[right] in dic.keys():
                    dic[s[right]] -= 1
                right += 1

        print(answer)
        if answer is None:
            return ""
        return answer