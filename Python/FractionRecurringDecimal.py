# https://www.geeksforgeeks.org/find-recurring-sequence-fraction/
class Solution(object):
    def fractionToDecimal(self, a, b):
        # if num is 0, then ans is 0
        if a == 0:
            return str(0)
        # if b divides a, then return quotient
        if a % b == 0:
            return str(a / b)

        res = ''
        # if sign is negative, add it before hand
        if a * b < 0:
            res += '-'

        # now sign doesnt matter for a and b
        a = abs(a)
        b = abs(b)

        # add quotient and '.' as you know the answer is going to be fractions
        res += str(int(a / b))
        res += '.'

        # key - remainder value, value - index of the result where we encountered this value
        dic = dict()
        r = a % b
        # get the last index so far
        i = len(res)
        while r != 0:
            if r not in dic.keys():
                dic[r] = i
            else:
                # we found a remainder that was present in the dic keys
                i = dic[r]
                # i is the starting point of the repeat seq - so we need to get everything up till 'i'
                # res[:i] = '-0.' and then we add the brackets to mark repeat seq and we pass res[i:]
                # ie - the start of the repeat seq till the end of the repeat seq
                res = res[:i] + '(' + res[i:] + ')'
                return res
            # if we were doing a division like 4/5
            # we would have gotten r = 4 the first time, which we convert to 40, then divide by 5
            # so we get '8' as our "quotient" which is added to the res, then we get remainder 40 % 5 = 0
            # set that to new r, so we exit in the next iteration
            r = r * 10
            res += str(int(r / b))
            r = r % b
            i += 1
        return res
s = Solution()
# s.fractionToDecimal(-1, 11)
s.fractionToDecimal(-22, 7)