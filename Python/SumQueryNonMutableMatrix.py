# https://www.youtube.com/watch?v=PwDqpOMwg6U&index=40&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr
'''
Given 2D array, find sum of a sub matrix within the array
'''
class Solution(object):
    def sumfind(self, arr, start, end):
        # here 2nd and 3rd arguments are top left and bottom right corner of the matrix
        m = len(arr)
        n = len(arr[0])
        # why m + 1 and n + 1, it makes the calculation simpler
        # temp holds the cumulative sum matrix from 0,0 to i-1,j-1 in the matrix
        temp = [[None] * (n + 1) for x in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i is 0 or j is 0:
                    temp[i][j] = 0
                    continue
                # equals current array element + whatever we get from top,left - what we double added
                temp[i][j] = arr[i-1][j-1] + temp[i-1][j] + temp[i][j-1] - temp[i-1][j-1]

        # why +1, we're converting this to the new matrix format
        row1 = start[0] + 1
        col1 = start[1] + 1
        row2 = end[0] + 1
        col2 = end[1] + 1

        # some random formula
        ans = temp[row2][col2] + temp[row1-1][col1-1] - temp[row1-1][col2] - temp[row2][col1-1]
        print("answer is ", ans)
        return ans

s = Solution()
s.sumfind([[2,0,-3,4],[6,3,2,-1],[5,4,7,3],[2,-6,8,1]], (1,2), (3,3))
