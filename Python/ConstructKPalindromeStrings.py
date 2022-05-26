# https://leetcode.com/problems/construct-k-palindrome-strings
from collections import defaultdict
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        def isPalindrome(string):
            return string == string[::-1]
        
        # worst case, we can break 's' into 1 char each and each char is a palindrome by itself
        # but if we still fall short in generating the sufficient number of palindromes even after char
        # level break, then we can return false
        if len(s) < k:
            return False
        
        '''
        palindromes can be of 2 types - odd and even
        odd palindromes -- abcdcba, madam, bob, civic
        even palindromes -- hannah, aaaa, baab
        
        notice that in odd palindromes, there can be ONLY 1 char that is odd count
        example - 'madam' -- only 'd' is odd counted
        
        notice that in even palindromes, all characters must be even counted
        example - 'hannah' -- each of 'h', 'a' and 'n' appear twice
        
        let's say in a string input (may not be palindrome), there are multiple odd counted characters
        l --> 3
        m --> 3
        n --> 1
        o --> 5
        and there are other chars that are even counted, say 'a' appears 4 times, 'e' appears 10 times etc.
        
        say from this string, we had to create 3 palindromes using ALL chars of the string
         p1    p2    p3
        ----  ----  ----
        
        now focus on the odd counted characters:
        2 out of 3 of 'l' can be distributed in either p1, p2, or p3
        2 out of 3 of 'm' can be distributed in either p1, p2, or p3
        4 out of 5 of 'o' can be distributed in either p1, p2, or p3
        
        in effect, the distribution of these even counts of 'l', 'm', 'o' are as if we're distributing
        other even characters of the string (like 'a' or 'e') evenly into one of p1, p2, or p3
        
        now we're left with:
        l --> 1
        m --> 1
        n --> 1
        o --> 1
        
        these are what will help form 'odd' palindromes, because remember - 
        odd palindromes can have ONLY 1 char that has odd count
        
        we can distribute 3 out of 'l', 'm', 'n', 'o' into p1, p2 and p3, but we can't distribute the 4th!
        If we attempted to, one of p1, p2, p3 will no longer be a palindrome!
        
        so in general, if the number of odd counted chars > k, then we can't create k palindromes
        if its <= k, then we can. Why?
        
        instead of l,m,n,o -- we just had l,m and had to still create 3 palindromes
        then 2 out of 3 palindromes will be 'odd' palindromes (the ones that contain the 'l' and 'm')
        the last one will be an even palindrome!
        '''
        dic = defaultdict(int)
        for i in list(s):
            dic[i] += 1
        
        oddCounts = [v % 2 for v in dic.values()]
        
        if sum(oddCounts) > k:
            return False
        return True