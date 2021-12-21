# https://www.geeksforgeeks.org/meta-strings-check-two-strings-can-become-swap-one-string/
class Solution(object):
    def metaString(self, a, b):
        if len(a) != len(b):
            return False

        # if the 2 strings are same, they are not meta strings as there is no need to swap
        if a == b:
            return False

        i = 0
        count = 0
        prev = curr = -1
        while i < len(a):
            if a[i] != b[i]:
                count += 1

                if count > 2:
                    return False

                # this will happen twice
                # the first time around prev will be -1, curr will be the first mismatched index
                # the second time prev will be this prev value of curr, and curr will be 2nd mismatched index
                # once we've found these 2 mismatched indexes, count is 2
                # if this mismatch happens again, count will become 3 and we will exit with false
                prev = curr
                curr = i
            i += 1

        # now count is 2
        # now we have to check if we swap out these 2 mismatched indices, do the 2 strings become the same
        # lets do this swap on b
        b = list(b)
        temp = b[prev]
        b[prev] = b[curr]
        b[curr] = temp
        b = ''.join(b)

        # we swapped b, now a and b should match
        if a == b:
            return True
        return False

s = Solution()
print(s.metaString("geeks", "keegs"))
print(s.metaString("abhisha", "abhi"))
print(s.metaString("geekss", "ksegse"))
print(s.metaString("aaaa", "aaaa"))
print(s.metaString("aaba", "baaa"))