# Given a string s, return all palindromic subsequences of s.
# Example 1:
# Input: "abac"
# Output: ["a", "b", "c", "aa", "aba"]

def AllPalindromicSubsequences(s):
    n = len(s)
    res = set()
    # if len of string (n) = 2, we need to generate binary strings 00, 01, 10, 11 to get all combinations of chars in the string
    # To generate these we can use numbers from 2^2 to 2^3-1, ie, 4 to 7 - that will give us 100, 101, 110, 111 and we can strip off first bit.
    
    # the reason we can't use numbers from 0 to 2^n is because we get
    # the binary representation of 0, 1, ... n as 0, 1, 01, 10, 11 etc, we don't get all full n digits
    # and we need the full n digits to represent the string

    # that is why we use 2^n to 2^(n+1)-1 range to generate the binary strings 
    # notice the for loop has end range at 2^(n+1) which will naturally have last iteration at 2^(n+1) - 1
    for num in range(2**n, 2**(n+1)):
        # we get all the numbers in binary form 000 001 010 011.. 111
        # we chop off first 3 chars because we have the prefix '0b' which takes 2 chars and the 3rd char which we strip as described above
        # example, bin(7) will give us 0b111 and since we're considering a 2 length string (say "ab"), we just need the last "11"
        
        binNum = bin(num)[3:]
        
        print()
        print(f"bin(num) is {bin(num)}")
        print(f"binNum is {binNum}")

        subSeq = ""
        
        # go through each number in binary format and check of 1's in the number
        # only add corresponding index chars from the original string
        for idx, ch in enumerate(binNum):
            if ch == '1':
                subSeq += s[idx]

        # check if the subsequence string that we generated is a palindrome
        print(f"checking subSeq: {subSeq}")
        if subSeq and subSeq == subSeq[::-1]:
            res.add(subSeq)
    
    return list(res)
        
print(AllPalindromicSubsequences("abac"))