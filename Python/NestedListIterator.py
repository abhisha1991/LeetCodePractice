# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


# https://leetcode.com/problems/flatten-nested-list-iterator/description/
class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nlist = nestedList
        self.first = None
        self.res = []
        self.count = 0
        self.temp = []

    def next(self):
        """
        :rtype: int
        """
        # this is really not needed, however, since the answer is expected in a certain format, hence temp is kept
        # otherwise answer is stored in self.res
        if len(self.temp) > 0:
            ele = self.temp[0]
            self.temp = self.temp[1:]
            return ele

        self.count = 0
        # in case of a complex list, count stores the number of elements we flattened, for ex - [5, [1,[2,3]]],
        # the number of count will be 3 for [1,[2,3]]
        ele = self.nextHelper(self.first)
        print("ele is", ele)
        if type(ele) is list:
            if len(ele) is 0:
                return None
            self.temp.extend(self.res[-self.count:])
            ele = self.temp[0]
            print("new assigned ele", ele)
            print("old temp", self.temp)
            self.temp = self.temp[1:]
            print("new temp", self.temp)

        return ele

    # this is basically a dfs that happens if n is not an int (ie - if it is a list)
    def nextHelper(self, n):
        if n.isInteger():
            self.res.append(n.getInteger())
            self.count += 1
            print(self.res)
            return self.res[-1]
        else:
            tmp = n.getList()
            for i in tmp:
                self.nextHelper(i)
            return self.res[-self.count:]

    def hasNext(self):
        """
        :rtype: bool
        """
        # again, temp was not necessary
        if len(self.temp) > 0:
            return True

        if len(self.nlist) == 0:
            return False
        # stores the first element to tackle
        self.first = self.nlist[0]
        if len(self.nlist) == 1:
            self.nlist = []
        else:
            self.nlist = self.nlist[1:]
        return True


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())