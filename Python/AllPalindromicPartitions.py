# http://www.geeksforgeeks.org/given-a-string-print-all-possible-palindromic-partition/
# Not the same problem but similar: https://www.youtube.com/watch?v=lDYIvtBVmgo&t=601s

def allPalindromicPartitions(a):
    lena = len(a)
    partitions = list()
    list1 = list(a)
    partitions.extend(list1)
    for i in range(2, lena + 1):
        for j in range(0, lena - i + 1):
            b = a[j:j+i]
            if checkIfStringIsPalindrome(b):
                partitions.append(b)

    return partitions


def checkIfStringIsPalindrome(b):
    lenb = int(len(b)/2)
    if len(b) % 2 == 0:
        first = b[:lenb]
        second = b[lenb:]
    else:
        first = b[0: lenb]
        second = b[lenb + 1:]

    if second[::-1] == first:
        return True
    else:
        return False



allPalindromicPartitions('nitin')

# http://www.geeksforgeeks.org/given-a-string-print-all-possible-palindromic-partition/
# Watch out below for a very imp concept - in reversed function!!

# Not optimal - this is O(n2)


def all_palindromes(arr):
    arr = list(arr)
    result = []
    i = 2
    while i <= len(arr):
        j = 0
        while j + i <= len(arr):
            temp = arr[j:j + i]
            if is_palindrome(temp):
                result.append(''.join(temp))
            j += 1
        i += 1

    for i in arr:
        result.append(i)

    return result


def is_palindrome(temp):
    # YOU MUST CONVERT REVERSED BACK TO A LIST, OTHERWISE THIS RETURNS FALSE
    return temp == list(reversed(temp))


print(all_palindromes("nitin"))

