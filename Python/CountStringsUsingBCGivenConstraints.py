# https://www.geeksforgeeks.org/count-strings-can-formed-using-b-c-given-constraints/
class Solution(object):
    def __init__(self):
        self.res = 0

    def countStr(self, charCount, bCount, cCount):

        if bCount < 0 or cCount < 0:
            return 0

        if charCount is 0:
            return 1

        if bCount == cCount == 0:
            return 1

        self.res = self.countStr(charCount - 1, bCount, cCount)
        self.res += self.countStr(charCount - 1, bCount - 1, cCount)
        self.res += self.countStr(charCount - 1, bCount, cCount - 1)

        return self.res

s = Solution()
print(s.countStr(3, 1, 2))
