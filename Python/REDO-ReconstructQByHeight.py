#https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89407/Python-Documented-solution-in-O(n*n)-time-that-is-easy-to-understand
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda (h, k): (-h, k))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue