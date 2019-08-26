#https://leetcode.com/problems/di-string-match/

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        i,j,result = 0,len(S),[]

        for char in S:
            if char=='I':
                result.append(i)
                i+=1
            else:
                result.append(j)
                j-=1
        result.append(j)
        return result
