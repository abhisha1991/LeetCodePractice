"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
# https://leetcode.com/problems/employee-importance/submissions/
from collections import defaultdict
class Solution(object):
    def __init__(self):
        self.dic = defaultdict(list)
        self.ans = 0
        
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        for i in employees:
            self.dic[i.id] = [i.importance, i.subordinates]
        
        self.helper(id)
        return self.ans
        
    def helper(self, id):
        self.ans += self.dic[id][0]
        for i in self.dic[id][1]:
            self.helper(i)