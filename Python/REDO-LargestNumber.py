#https://leetcode.com/problems/largest-number/description/
class Solution:
    # @param {integer[]} nums
    # @return {string}
    # https://leetcode.com/problems/largest-number/description/
    class Solution:
        # @param {integer[]} nums
        # @return {string}

        def largestNumber(self, nums):
            # define a lambda function that compares the concat of 2 strings
            comp = lambda a, b: 1 if a + b > b + a else -1 if b + a > a + b else 0
            # make nums as string inputs for each element of nums
            nums = map(str, nums)
            # sort nums such that we override the functionality of the comparator function in sort
            # this is the most critical line
            nums.sort(comp, reverse=True)
            print(nums)
            # concat the string, convert to nums, convert back to string and return
            # why the need to convert to int and then back to string? because imagine a case like '00',
            # the output should be 0, if we don't convert to int, we will get the output as '00'
            return str(int(''.join([x for x in nums])))

    ## wrong solution!!!
    def largestNumber2(self, nums):
        result = ""
        desc_list = [9,8,7,6,5,4,3,2,1]
        for i in desc_list:
            candidates = [j for j in nums if int(str(j)[0:1]) == i]
            if len(candidates) is 0:
                continue
            else:
                if len(candidates) == 1:
                    num = max(candidates)
                if len(candidates) > 1:
                    # This is a wrong solution as simple sorting wont work, example [121,12] => 12121, not 12112
                    candidates = sorted(candidates, reverse=True)
                    num = ''.join(str(k) for k in candidates)
                result = result + str(num)

        return result

    # not optimal, dont use!!
    def largestNumber(self, nums):
        maximum = ''
        import itertools
        for x in itertools.permutations(nums, len(nums)):
            tmp = ''.join(str(k) for k in x)
            if tmp > maximum:
                maximum = tmp

        print(maximum)
        if maximum[:1] is '0' and maximum[len(maximum) - 1:len(maximum)] is '0':
            return 0
        else:
            return maximum

s = Solution()
s.largestNumber(nums=[1,2,3,4,5,6,7,8,9,0])