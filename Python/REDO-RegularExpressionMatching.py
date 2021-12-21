# https://www.youtube.com/watch?v=l3hda49XcDE
# https://leetcode.com/problems/regular-expression-matching/description/
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)

        arr = [[False] * (n + 1) for x in range(m + 1)]
        # empty pattern empty string
        arr[0][0] = True
        # first column is all false except [0][0] because you're matching an empty pattern with a string

        # remember that because we have added a '' to both pattern and string,
        # hence current index is i-1, j-1 for 's' and 'p'
        # for arr, current index is i,j
        for i in range(m + 1):
            for j in range(n + 1):
                if i == j == 0:
                    continue

                # empty string with a given pattern
                if i == 0:
                    # first row needs to be handled specially if string is 'aa' and pattern is 'a*' or 'a*b*' etc.
                    # if pattern is not *, it cant match with a character as our input string is empty
                    if p[j - 1] != '*':
                        arr[0][j] = False
                    else:
                        # consider a case like '' vs 'a*', when we do j-2,
                        # we are matching empty input string with empty pattern, ie arr[0][0], which is true
                        arr[0][j] = arr[0][j - 2]
                    continue

                # if current element of pattern is same as current element of string,
                # then just remove these 2 and check this for rest of result [i-1][j-1]
                if i > 0 and j > 0 and ((s[i - 1] == p[j - 1]) or p[j - 1] == '.'):
                    arr[i][j] = arr[i - 1][j - 1]
                    continue

                if i > 0 and j > 1 and p[j - 1] == '*':
                    # include 0 occurances of the element corresponding to *
                    # example, xa* vs x => remove a*, ie, column j-2
                    arr[i][j] = arr[i][j - 2]
                    if arr[i][j]:
                        continue

                    # watch minute 11 of the above video (alternate explanation below)
                    # if arr[i][j] is still false, say xa* vs xa => remove a* means p = 'x' and s = 'xa', which is false
                    # if element before * matches the last element of string
                    # then we have to check if last char of string, ie, 'a' is same as char before '*', ie 'a'
                    # the p[j-2] == '.' condition handles the following case 'x.*' vs 'xa', here '.' == 'a' is true
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        # look above and "or" it with current
                        arr[i][j] = arr[i][j] or arr[i - 1][j]

                    continue

                # default case, doesnt matter,
                # we've already initialized everything to false, so having/not having this has no effect
                arr[i][j] = False

        return arr[m][n]