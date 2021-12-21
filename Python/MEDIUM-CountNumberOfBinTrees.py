# https://www.youtube.com/watch?v=RUB5ZPfKcnY&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=41
# https://www.youtube.com/watch?v=YDf982Lb84o&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=37
# CATALAN NUMBER
'''
say you had 5 elements in a tree, whose pre-order is 10,11,12,13,14
Find number of all possible binary trees

let T[i] be number of possible trees when number of elements are i
T[0] = 1
T[1] = 1
T[2] = 2
 A       A
 \  AND /
  B    B
T[3] = 5
A         A       A        A      A
 \ AND   /  AND  / \  AND /  AND  \
 B      B       B  C     B        B
  \    /                 \       /
  C   C                  C      C
'''
class Solution(object):
    def countBinTrees(self, n):
        t = dict()
        t[0] = 1
        t[1] = 1
        for i in range(2, n+1):
            t[i] = 0
        # i is the index corresponding to the number of elements whose preorder is given
        for i in range(2, n+1):
            # j plays the role of shifting elements in the children of the preorder
            '''
                10                 vs           10                     10           etc...
                /\                              /\                     / \
            {11}  {12,13,14}             {11,12}  {13,14}    {11,12,13}  {14}
            the above will be for i = 4, 10 is the root of the tree, has 4 children, which can be shifted
            '''
            for j in range(0, i):
                # t[5] = sum of each of the scenario trees above
                # ie - t[5] = {t[0] * t[4]} + {t[1] * t[3]} + {t[2] * t[2]} + {t[3] * t[1]} + {t[4] * t[0]}
                t[i] += t[j] * t[i-j-1]
        return t[n]

s = Solution()
print(s.countBinTrees(5))