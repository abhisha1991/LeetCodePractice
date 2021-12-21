# https://leetcode.com/problems/palindrome-number/submissions/
# read solution from epi - section 4.9
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if a number is negative it clearly cant be a palindrome
        if x < 0:
            return False
        # if number is 0 it is a palindrome
        if x == 0:
            return True
        
        # consider 11211 as example
        # num digits = math.log10(121) = 4 + 1, ie 5
        numdigits = int(math.log10(x)) + 1
        # msdmask is most significant digit mask
        # initially, this will be 10000, ie 10^4
        # msdmask is the mask that we use to isolate and remove the first digit
        msdmask = 10**(numdigits-1)
        # you need to only run this till the middle of the length of x
        # why? that's what we do in a regular palindromic string, compare till half string length, so same concept with number
        for i in range(int(numdigits/2)): 
            # if the msd and the lsd are different, its not a palindrome
            # in case of 11211, this comparison will be between 1 and 1
            
            if int(x / msdmask) != x % 10:
                return False
            
            # next we attempt to make 11211 to 121, removing msd and lsd
            # we do this by first converting x to the remainder when divided by msdmask
            # so remainder when 11211 / 10000 = 1211
            # next, we take 1211 and remove lsd, how? do division by 10 and take quotient
            
            x = x % msdmask
            x = int(x / 10)
            # after this point, number is converted from 11211 to 121
            # lastly, update msdmask for new number 121, what will this be? should be 100
            # how to get new msdmask? divide by 100, why?
            # because first and last digits are gone now (11211 --> 121), so we've removed 10^2 effectively 
            msdmask = int(msdmask / 100)
        return True