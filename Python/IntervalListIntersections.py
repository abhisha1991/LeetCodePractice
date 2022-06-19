# https://leetcode.com/problems/interval-list-intersections
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        
        i = 0
        j = 0
        n1 = len(firstList)
        n2 = len(secondList)
        res = []
        while i < n1 and j < n2:
            a = firstList[i]
            b = secondList[j]
            
            startMax = max(a[0], b[0])
            endMin = min(a[1], b[1])
            
            # if the intersection has start and end that are valid
            # notice the equal to as well, so this includes intervals like [5,5]
            if endMin >= startMax:
                res.append([startMax, endMin])
            
            # notice that we are not doing increment of i, j in if/else manner
            # we are independently incrementing i,j
            # why? because we could have an equality clash on endMin
            # for example, a = [4,5], b = [3,5] --> endMin for both is 5, so we want to increment both lists
            if endMin == a[1]:
                i +=1
                
            if endMin == b[1]:
                j +=1
        
        return res