# https://www.youtube.com/watch?v=3ZDZ-N0EPV0
# https://leetcode.com/problems/wildcard-matching/description/
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # if both string and pattern are 0 length
        if len(s) == len(p) == 0:
            return True

        # if string was "" and pattern was "*"
        setp = set(x for x in p)
        if len(s) == 0 and setp.pop() == '*':
            return True

        # if one is empty and other is not
        if len(s) == 0 or len(p) == 0:
            return False

        # handling a case where string is "ho" and pattern is "***ho"
        temp = "*"
        count = 0
        if p[0] == '*':
            for i in p:
                if i == '*':
                    count += 1
                else:
                    break

            # converting the pattern to become "*ho" from "***ho"
            p = temp + p[count:]

        m = len(s) + 1
        n = len(p) + 1
        arr = []
        # by default everything is false
        for i in range(m):
            temp = [False] * n
            arr.append(temp)

        for i in range(m):
            for j in range(n):
                # 2 empty strings are always true
                if i == 0 and j == 0:
                    arr[i][j] = True
                    continue

                # empty pattern matched with string is always false
                if j == 0:
                    arr[i][j] = False
                    continue

                # empty string with pattern such that first element of pattern is '*'
                if j == 1 and i == 0 and p[j - 1] == '*':
                    arr[i][j] = True
                    continue

                # empty string with pattern p
                if i == 0:
                    arr[i][j] = False
                    continue

                # if the string and pattern last elements are the same OR
                # if the last pattern char can take on any letter (can be forced to become similar to string's last char)
                # example, "xa" and "x?" is the same as comparing "x" with "x" as '?' matches 'a'
                # in this case, just let this be whatever you would have achieved without the last characters in place
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    arr[i][j] = arr[i - 1][j - 1]
                    continue

                # watch 10:00 to 10:30 in the video above
                # or basically, we're saying that "xay" vs "x?y*" -> implies
                # we can make '*' represent no character in which case we check if "xay" matches "x?y",
                # which we get from arr[i][j-1] (j-1 means we remove last element from pattern, ie - remove '*')
                # OR
                # we make '*' represent 1 or more character, ie - "xa" vs "x?y", which is arr[i-1][j-1]
                # OR
                # we make '*' eat up 1 character but keep '*' to eat up more characters - 'xa' vs 'x?y*' or arr[i-1][j]
                # there's no need to find arr[i-2][j], arr[i-3][j] etc.... because the above would give the result for all
                elif p[j - 1] == '*':
                    arr[i][j] = arr[i - 1][j] or arr[i][j - 1]

                else:
                    arr[i][j] = False

        return arr[m - 1][n - 1]
