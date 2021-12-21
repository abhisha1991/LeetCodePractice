# https://leetcode.com/problems/count-primes/
# look into time complexity for this
class Solution(object):
    # not efficient
    def countPrimes2(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(n):
            if self.isprime(i):
                count +=1
        return count
    
    
    def isprime2(self, num):
        if num <=1:
            return False
        
        x = 2
        while x * x <= num:
            if num % x == 0:
                return False
            x +=1
        return True
    
    # seive of Eratosthenes, efficient
    def countPrimes(self, n):
        if n <= 1:
            return 0
        # assume all numbers are prime. 
        # In the end we will just return count where this array is true
        isitprime = [True] * n
        # 0 and 1 are not primes, we know
        isitprime[0] = False
        isitprime[1] = False
        count = 0
        
        i = 2
        while i * i < n:
            if not isitprime[i]:
                continue
            j = i*i
            while j < n:
                isitprime[j] = False
                # notice j is being incremented as j = j+i, why? 
                # because we are marking multiples of i, starting at j as false
                j +=i
            i +=1
        
        for x in range(n):
            if isitprime[x]:
                count +=1
        return count
        
        