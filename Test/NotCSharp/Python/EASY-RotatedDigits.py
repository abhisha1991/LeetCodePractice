# https://leetcode.com/problems/rotated-digits/submissions/
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        dic = dict()
        dic[0] = 0
        dic[1] = 1
        dic[2] = 5
        dic[3] = '#'
        dic[4] = '#'
        dic[5] = 2
        dic[6] = 9
        dic[7] = '#'
        dic[8] = 8
        dic[9] = 6
        count = 0
        for i in range(1, N+1):
            digits = [int(x) for x in str(i)]
            num = ''
            flag = True
            for d in digits:
                if dic[d] == '#':
                    flag = False
                    break
                else:
                    num += str(dic[d])
            if flag and num and int(num) != i:
                count +=1
        return count