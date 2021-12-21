from collections import defaultdict
# https://www.youtube.com/watch?v=cIOxZ7bNh7w

class Solution:
    def letterCombinations(self, digits):
        """
                234
                 ""
             /    |    \
            a     b     c
           /|\   /|\   /|\
          d e f d e f d e f
        """
        dic = defaultdict(list)
        dic["2"] = ["a", "b", "c"]
        dic["3"] = ["d", "e", "f"]
        dic["4"] = ["g", "h", "i"]
        dic["5"] = ["j", "k", "l"]
        dic["6"] = ["m", "n", "o"]
        dic["7"] = ["p", "q", "r", "s"]
        dic["8"] = ["t", "u", "v"]
        dic["9"] = ["w", "x", "y", "z"]
        dic["0"] = [""]
        dic["1"] = [""]

        combinations = []

        def recurse(digs, path_so_far):
            if len(digs) == 0:
                combinations.append(path_so_far)
                return

            first = digs[0]
            rest = digs[1:]
            for i in dic[first]:
                recurse(rest, i + path_so_far)

        recurse(str(digits), "")
        print(combinations)


s = Solution()
s.letterCombinations(23456710)