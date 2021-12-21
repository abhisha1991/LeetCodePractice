# https://www.youtube.com/watch?v=jwzo6IsMAFQ
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# worst case below algo is o(n2), o(n) is given here: https://www.youtube.com/watch?v=1pOqgdO327Q
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def __init__(self):
        self.serial = []
        self.idx = 0

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.shelper(root)
        print(self.serial)
        return self.serial

    def shelper(self, root):
        if root is None:
            # this step is key, to append the null values as '#'
            self.serial.append(str("#"))
            return

        # note how we are doing a pre order serializer, this is important as it would be linked to the deserializer
        self.serial.append(str(root.val))
        self.shelper(root.left)
        self.shelper(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return []

        return self.dhelper(data)

    def dhelper(self, data):
        if self.idx == len(data) or data[self.idx] == '#':
            self.idx += 1
            return None

        # note how the deserializer also does a pre-order construction, same as serializer
        # note that pre-order is convenient, as first element of array is root
        # if we did postorder, then we would have to start from the other side 'LRN',
        # worse if we did inorder, we will need to figure out where to start and we cant increment index simply to get left/right subtree
        root = TreeNode(data[self.idx])
        self.idx += 1
        root.left = self.dhelper(data)
        root.right = self.dhelper(data)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))