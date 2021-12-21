# https://leetcode.com/problems/rectangle-area/submissions/
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        total = abs((C-A)*(D-B)) + abs((G-E)*(H-F))
        return total - self.intersectar(A, B, C, D, E, F, G, H)
    
    def intersectar(self, a, b, c, d, e, f, g, h):
        if e >= c or g <= a or h <= b or f >= d:
            return 0
        '''
        r1w = abs(c-a)
        r1h = abs(d-b)
        r2w = abs(g-e)
        r2h = abs(h-f)
        '''
        l = abs(max(a,e) - min(c,g))
        h = abs(max(b,f) - min(d,h))
        return l *h