# https://www.geeksforgeeks.org/generate-all-binary-strings-from-given-pattern/
# something like generate all subsets
class Solution(object):
    def __init__(self):
        self.res = []

    def generateBin(self, bins):

        self.helper(list(bins), 0)
        return self.res

    def helper(self, bins, idx):
        if idx == len(bins):
            self.res.append(''.join(bins))
        else:
            if bins[idx] == '?':
                # replace this index by 0 then recurse
                bins[idx] = '0'
                self.helper(bins, idx + 1)
                # replace this index by 1 then recurse
                bins[idx] = '1'
                self.helper(bins, idx + 1)
                # set everything back to how it was
                bins[idx] = '?'
            else:
                self.helper(bins, idx + 1)


s = Solution()
print(s.generateBin('1??0?101'))

