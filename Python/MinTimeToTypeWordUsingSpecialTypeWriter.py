# https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter
from collections import defaultdict
class Solution:
    def minTimeToType(self, word: str) -> int:
        prev = 'a'
        # we at least need len word seconds to write out the word
        # even if we're at the same letter, it takes a second to write
        ans = len(word)
        for i in word:
            num_prev = ord(prev)
            num_cur = ord(i)
            
            steps = abs((num_cur - num_prev) % 26)
            # we can take steps in clockwise and anti clockwise direction
            ans += min(steps, 26 - steps)
            
            prev = i
            
        return ans