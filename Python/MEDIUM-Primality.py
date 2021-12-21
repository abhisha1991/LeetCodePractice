# http://www.geeksforgeeks.org/primality-test-set-1-introduction-and-school-method/
import math

# p is the number of test cases
p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    isPrime = True
    if n == 2 or n == 1:
        print('Prime')
        continue
    if n % 2 == 0 or n % 3 == 0:
        print('Not prime')
        continue

    i = 5
    is_prime = True
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            # here i is essentially 6k-1, i+2 is 6k+1, why, see below
            print('Not Prime')
            is_prime = False
            break
        else:
            i += 6

    if is_prime:
        print('Prime')



'''
static bool isPrime(int n)
{
    // Corner cases
    if (n <= 1)  return false;
    if (n <= 3)  return true;
 
    
    if (n%2 == 0 || n%3 == 0) return false;
 
    // why this? any prime number is of the form 6k +/- 1, why?
    // Number cannot be 6k + 2 => div by 2, cant be 6k+3 or 6k+4, the only one left is 6k+5, which is essentially 6k-1
    for (int i=5; i*i<=n; i=i+6)
        if (n%i == 0 || n%(i+2) == 0)
        // Here i is essentially 5 -> 6 * 1 - 1, next time, i will be 11, 6 * 2 - 1 etc
        // Which means that i is 6k-1, i + 2 is 6k+1
           return false;
 
    return true;
    
}

'''