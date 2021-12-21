# https://leetcode.com/problems/plus-one/description/
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = list(reversed(digits))
        digits.append(0)
        remainder = 0
        carry = 0
        digits[0] = digits[0] + 1
        print(digits)
        for i in range(len(digits)):
            num = digits[i] + carry
            print("num", num)
            remainder = num % 10
            print("remainder", remainder)
            carry = int(num / 10)
            print("carry", carry)
            digits[i] = remainder
            print("digits[i]", i, digits)

        digits = list(reversed(digits))
        if digits[0] == 0:
            digits = digits[1:]
        return digits