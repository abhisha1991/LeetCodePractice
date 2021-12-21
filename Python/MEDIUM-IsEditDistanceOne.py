# https://www.geeksforgeeks.org/check-if-two-given-strings-are-at-edit-distance-one/
# was asked in bing!!!
class Solution(object):
    def isEditDistOne(self, a, b):
        count = 0

        m = len(a)
        n = len(b)
        i = 0
        j = 0
        if abs(m-n) > 1:
            return False

        while i < m and j < n:
            if a[i] == b[j]:
                i += 1
                j += 1
                continue
            else:
                if count == 1:
                    return False

                # first time that they are different
                count += 1
                if m > n:
                    i += 1
                elif m < n:
                    j += 1
                else:
                    i += 1
                    j += 1

        if i < m or j < n:
            count += 1

        print(count)
        return count == 1

s = Solution()
print(s.isEditDistOne("plea", "leap"))
print(s.isEditDistOne("abc", "ab"))
print(s.isEditDistOne("abc", "acb"))
print(s.isEditDistOne("plea", "ple"))
print(s.isEditDistOne("geeks", "geeke"))
