# https://leetcode.com/problems/decode-ways/description/
# https://www.youtube.com/watch?v=aCKyFYF9_Bg
# Below solution implements idea from the video, however, we're not getting correct results for all OJ cases
class Solution(object):
    def __init__(self):
        self.dic = dict()
        for i in range(10):
            self.dic[i] = 1
        self.dic[''] = 1

        self.count = 0

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        lens = len(s)
        if lens is 0:
            return 0

        if s[0] == '0':
            return 0

        if lens is 1:
            return lens

        self.count = self.helper(s)
        return self.count

    def helper(self, s):
        lens = len(s)
        if lens is 0:
            return self.dic['']

        if int(s) in self.dic.keys():
            return self.dic[int(s)]

        last = s[lens - 1:]
        lasttwo = s[lens - 2:]

        cnt1 = 0
        cnt2 = 0
        if int(last) > 0 and int(last) <= 9:
            # if last char was 1-9
            cnt1 = self.helper(s[:lens - 1])
            len_temp = len(s[:lens - 1])
            if len_temp is not 0:
                self.dic[int(s[:lens - 1])] = cnt1

        if int(lasttwo) <= 26:
            # if last 2 char was 10-26
            cnt2 = self.helper(s[:lens - 2])
            len_temp = len(s[:lens - 2])
            if len_temp is not 0:
                self.dic[int(s[:lens - 2])] = cnt2

        return cnt1 + cnt2

