# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/

class Tree(object):
    def __init__(self, val, order):
        self.val = val
        self.left = None
        self.right = None
        # number of nodes to your right that are smaller than you
        self.smaller = 0
        # the order in which you were inserted into the tree
        self.order = order


class Solution:
    def __init__(self):
        self.dic = dict()
        # count has final answer
        self.count = []
        self.t = None

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) is 0:
            return []
        if len(nums) is 1:
            return [0]
        if len(nums) is 2:
            if nums[0] > nums[1]:
                return [1, 0]
            else:
                return [0, 0]

        # insert first element of list with insert order '0'
        self.t = Tree(nums[0], 0)
        tree = self.t
        # insert the rest of the elements in the same order as they appear on the list
        for i in range(1, len(nums)):
            self.buildTree(tree, nums[i], i)

        # traverse through list and update the dictionary
        # dic key - order of insertion
        # dic value - number of elements to the right that are smaller than this element at index 'key'
        self.traverse(self.t)
        print(self.dic)
        # formatting - we need to return a list, not a dictionary
        for i in range(len(nums)):
            self.count.append(self.dic[i])

        print(self.count)
        return self.count

    def traverse(self, t):
        # any traversal, preorder, postorder, inorder will work here
        if t is None:
            return
        self.traverse(t.left)
        self.dic[t.order] = t.smaller
        self.traverse(t.right)

    def buildTree(self, tree, ele, i):
        if tree is None:
            return
        else:
            if ele < tree.val:
                # increment curent node's smaller count
                tree.smaller += 1

                '''
                imagine input like [5,2,6,1], here the tree is
                        5
                       / \
                      2   6
                     /
                    1 
                1. observe element '6' - the count for element 6 should be '1' as there is 1 number that is to the right of 6 which is < 6
                2. but if we dont do updateCount() below, the 'smaller' value for 6 will be 0, as 1 is inserted to the left of its parent '5'.
                3. if ele is < 5, then its less than all elements to the right of 5 in the tree
                4. therefore, traverse through the right part of the tree and increment smaller for each node iff order of node < order of current insert

                '''
                if tree.right is not None:
                    self.updateCount(tree.right, i)

                if tree.left is None:
                    tree.left = Tree(ele, i)
                else:
                    self.buildTree(tree.left, ele, i)
            elif ele >= tree.val:
                if tree.right is None:
                    tree.right = Tree(ele, i)
                else:
                    self.buildTree(tree.right, ele, i)

    def updateCount(self, tree, i):
        if tree is None:
            return
        if tree.order < i:
            tree.smaller += 1

        self.updateCount(tree.left, i)
        self.updateCount(tree.right, i)


s = Solution()
s.countSmaller([5,2,6,1])


# Correct solution - this is O(n2) though - takes too long, look at java code for the same file name - CountSmaller.
class Solution2(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == []:
            return []
        dic = dict()
        dic[len(nums) - 1] = 0

        for i in range(len(nums) - 2, -1, -1):
            temp = nums[i:]
            ele = nums[i] * -1
            temp[:] = [x + ele for x in temp]
            count = len([y for y in temp if y < 0])
            dic[i] = count

        result = []
        for k, v in dic.items():
            result.append(v)

        return result