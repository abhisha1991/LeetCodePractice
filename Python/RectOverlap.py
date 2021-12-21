class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        '''
        x axis constraints:
        
        rec2[0] >= rec1[2]
        if bottom left of 2nd rect is to the right of top right of 1st rect
        
        rec2[2] <= rec1[0]
        if top right of 2nd rect is to the left of bottom left of 1st rect
        
        y axis constraints:
        rec2[3] <= rec1[1]
        if top right of 2nd rect is below bottom left of 1st rect
        
        rec2[1] >= rec1[3]
        if bottom left of 2nd rect is above top right of 1st rect
        
        '''
        if rec2[0] >= rec1[2] or \
            rec2[2] <= rec1[0] or \
            rec2[3] <= rec1[1] or \
            rec2[1] >= rec1[3]:
            return False
        return True