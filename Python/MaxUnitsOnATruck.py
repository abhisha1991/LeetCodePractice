# https://leetcode.com/problems/maximum-units-on-a-truck/
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # sort box types by units highest to lowest
        boxTypes = sorted(boxTypes, key=lambda x: (x[1]), reverse=True)
        res = 0
        while truckSize > 0 and len(boxTypes) > 0:
            bt = boxTypes[0]
            # quantity of this box type
            q = bt[0]
            # number of units of this box type
            u = bt[1]
            
            if q > 0 and truckSize > 0:
                # if the trucksize can absorb this quantity completely
                # then add u * q to result
                # subtract capacity of truck size by q
                # remove the first boxtype with highest units, so the next boxtype can be picked
                if q <= truckSize:
                    boxTypes.pop(0)
                    res += u * q
                    truckSize -=q
                else:
                    res += u * truckSize
                    return res
        
        return res