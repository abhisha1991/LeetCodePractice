# https://leetcode.com/problems/find-the-closest-palindrome/
import heapq
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        # if n=7, then return 6 (lower number is preferred)
        if len(n) == 1:
            return str(int(n)-1)
        
        '''
        brute force solution - if we have n = 489
        
        we can go in the negative direction - 488, 487, 486, 485, 484 --> stop here since 484 is a palindrome
        we can go in the positive direction - 490, 491, 492, 493, 494 --> stop here since 494 is a palindrome
        
        now abs(489 - 484) is the same as abs(489 - 494), so we choose the lower of the 2 palindromes and return 484
        '''
        
        '''
        so the answer for 489 we know is 484 since we did the exercise above, but you can imagine having a number 'n'
        for whom the answer could be another number that is:
        1. the same number of digits as 'n' 
            like 489 and 484 both have 3 digits
            
            but in general, we'd have to include numbers like 101 or 999 as extreme points in the same digit length 'n'
            
            101 can be constructed as 10 ^ (digits-1) + 1 = 10^(3-1) + 1 = 101
            999 can be constructed as 10 ^ (digits) - 1 = 10^3 - 1 = 999
            
        2. one less digit than what we have in 'n' 
            say for a 3 digit n (say 100), we can have a 2 digit number that is the closest palindrome, say 99
            99 can be constructed as 10 ^ (digits-1) - 1 => 10^(3-1) - 1 = 99
        
        3. one more digit than what we have in 'n'
            say for a 3 digit n (say 999), we can have a 4 digit number that is the closest palindrome, say 1001
            1001 can be constructed as 10 ^ (digits) + 1 => 10^3 + 1 = 1001
        
        so we should add all these potential numbers that are each palindromes, into our candidate pool 
        '''
        
        digits = len(list(n))
        candidates = []
        # add same digit length palindrome candidates, example: 101, 999
        candidates.append(10 ** (digits-1) + 1)
        candidates.append(10 ** (digits) - 1)
        
        # add one digit less length palindrome candidates, example: 99
        candidates.append(10 ** (digits-1) - 1)
        
        # add one digit more length palindrome candidates, example: 1001
        candidates.append(10 ** (digits) + 1)
        
        # let's use a more complex example going forward to do our code: 48279
        
        mid = (digits+1)//2 # for 5 digits, this mid value will be 3
        
        # because we're only concerned with palindromes, thus lets break our number into a prefix and postfix
        # instead of processing the entire number all at once
        
        # and lets focus only on the prefix, from which we can derive the postfix
        # prefix will be first half of number, postfix will basically be reverse of prefix 
        # which will automatically make it into a palindrome
        
        # example if number is 48279 ==> then prefix is 482 
        pre = int(int(n) / 10 **  (digits - mid))
        
        # in fact we can have many prefixes in case our original one, ie, 482 doesn't turn out to generate a palindrome
        # we can actually have 3 immediate ones - 482, 483, 481 - these will have the highest probability of being closest to 'n'
        prefixes = [pre, pre + 1, pre - 1]
        for pf in prefixes:
            
            strpf = str(pf)
            # convert 482 to a list of char, ie, ['4', '8', '2']
            post = [strpf[i] for i in range(len(strpf))]
            
            # for a odd digit number 'n', like our example, 48279, we can get rid off the '2' in end
            # if n was even digit, like 4879, we would not
            # why? we're trying to derive postfix from prefix by reversing prefix, '2' was the middle element in 'n'
            # so we can't use '2' in the reversing
            if digits % 2 == 1:
                post.pop()
            
            # reverse the derived postfix, so we can append this to the prefix to generate our final number
            post = list(reversed(post))
            
            post = ''.join(post)
            pre = str(pf)
            
            # join the 2 strings
            num = pre + post
            # convert num to an integer
            num = int(num)
            
            # add this palindrome num to candidate list
            candidates.append(num)    
        
        
        mnDiff = sys.maxsize
        ans = []
        
        for c in candidates:
            diff = abs(c - int(n))
            # we want the closest number, not the number itself if it was a palindrome, for example n = '11'
            if diff == 0:
                continue
            
            # push to a heap and let the one with the lowest abs diff bubble to the top
            heapq.heappush(ans, (diff, c))
        
        return str(ans[0][1])