class Solution(object):
    def minlensubarry(self, arr, x):
        start = 0
        minlen = len(arr) + 1
        summ = 0
        for i in range(len(arr)):
            summ += arr[i]
            if summ > x:
                length = i - start + 1
                if length < minlen:
                    minlen = length

            s
dfvd