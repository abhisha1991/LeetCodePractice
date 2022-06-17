# https://leetcode.com/problems/next-greater-element-iii/
# https://leetcode.com/problems/next-permutation/
# https://leetcode.com/problems/next-palindrome-using-same-digits/
# the above are all the same basically
class Solution:
    def nextPalindrome(self, num: str) -> str:
        nums = [num[i] for i in range(len(num))]
        
        # nums with length 1 cannot have next greater palindrome
        if len(nums) == 1:
            return ""
        
        # since nums is a palindrome (given), we can focus only on first half of the number
        n = len(nums)
        # check if its an even length palindrome or not
        even = True if n % 2 == 0 else False
        
        # if its not an even length palindrome, get the mid element and store separately
        mid = nums[n//2] if not even else None
        
        # now let's deal only with the first half of nums, so lets shrink it to half and
        # go with the assumption as if this was our original number
        m = n//2
        nums = nums[:m]
        
        # find pos from right where the decreasing criteria breaks (this is borrowed from NextGreaterElement-III)
        # example, 564987 --> from the right, decreasing criteria breaks at digit 4, ie, pos = 2 
        pos = None
        for i in range(m-1, -1, -1):
            prev = nums[i-1]
            cur = nums[i]
            # if cur happens to be greater than the previous digit, then the criteria is broken
            if cur > prev:
                pos = i-1
                break
        
        # if we were unable to find a strictly decreasing criteria from the right, example, 321
        # then there cannot be a next larger permutation/number
        # pos will be < 0 for the cases where the first digit is the largest
        if pos == None or pos < 0:
            return ""
        
        # find the position of the digit to the right of pos that is just greater than nums[pos]
        nxtGreaterPos = None
        mn = sys.maxsize
        
        for i in range(pos+1, m):
            diff = ord(nums[i]) - ord(nums[pos])
            if diff > 0 and mn > diff:
                mn = diff
                nxtGreaterPos = i
        
        # swap the next greater number and the number at pos
        tmp = nums[pos]
        nums[pos] = nums[nxtGreaterPos]
        nums[nxtGreaterPos] = tmp
        
        # if we're not dealing with even length palindrome, we need to add 'mid' to the middle of nums, else we dont
        # but generally, we need to make nums back to its original size of 'n' instead of shortened half size 'm'
        # so we need to do something like nums = A + reversed(A)
        if not even:
            nums = nums[:pos+1] + sorted(nums[pos+1:])
            rev = list(reversed(nums))
            nums = nums + [mid] + rev
        else:
            nums = nums[:pos+1] + sorted(nums[pos+1:])
            rev = list(reversed(nums))
            nums = nums + rev
        
        return "".join(nums)