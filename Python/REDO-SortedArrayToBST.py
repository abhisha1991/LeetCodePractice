class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        # get the median
        mid = int(len(nums) / 2)

        # now the array is balanced on the left and right in terms of number of elements
        root = TreeNode(nums[mid])
        # build the left and right tree recursively
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root
