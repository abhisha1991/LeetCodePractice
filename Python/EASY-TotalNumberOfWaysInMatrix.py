# https://www.youtube.com/watch?v=GO5QHC_BmvM&index=38&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr
class Solution(object):
    def totalways(self, m, n):
        ways = [[None] * n for x in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    ways[i][j] = 1
                    continue

                ways[i][j] = ways[i-1][j] + ways[i][j-1]

        print(ways)
        print("Total number of ways with m and n are ", m, n, ways[m-1][n-1])

s = Solution()
s.totalways(2, 3)
s.totalways(20, 30)
s.totalways(4, 30)
s.totalways(1, 1)