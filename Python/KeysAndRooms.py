# https://leetcode.com/problems/keys-and-rooms/

class Solution(object):
    def __init__(self):
        self.visited = []
    
    
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        self.visited = [False] * len(rooms)
        self.search(0, rooms)
        
        return len([x for x in self.visited if x == False]) == 0
    
    def search(self, start, rooms):
        if self.visited[start]:
            return
        
        self.visited[start] = True
        for i in rooms[start]:
            self.search(i, rooms)