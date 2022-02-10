# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# https://leetcode.com/problems/flatten-nested-list-iterator
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):     
        self.ints = []
        self.flatten(nestedList)
        self.pos = 0
    
    # recursively keep flattening the list until you reach an integer
    def flatten(self, nestedList):
        for n in nestedList:
            if n.isInteger():
                self.ints.append(n.getInteger())
            else:
                self.flatten(n.getList())
                
    def next(self) -> int:
        val = self.ints[self.pos]
        self.pos +=1
        return val
    
    def hasNext(self) -> bool:
        return self.pos < len(self.ints)

'''
take an example like [1,[2,[4,5]]]
answer should be [1,2,4,5]

1st flatten call will add 1 to output, since 1 is integer
next element is [2, [4,5]] which is not an integer, so we enter into flatten([2, [4,5]])
2nd flatten will check first element [2, ...] of that list, see it is an integer and add "2" to output
next element is [4,5] which is not an integer, so we enter into flatten([4,5])
3rd flatten will check first element [4,..] of that list, see it is an integer and add "4" to output
next element is 5, which is an integer as well, so we add "5" to output

we come out of 3rd, 2nd and 1st flatten calls and output is [1,2,4,5]

'''
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())