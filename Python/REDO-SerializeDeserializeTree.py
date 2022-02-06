# https://www.youtube.com/watch?v=jwzo6IsMAFQ
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def __init__(self):
        self.idx = 0
        self.n = -1
        self.serial = []
        
    def serialize_rec(self, root):
        if root == None:
            self.serial.append(None)
            return
        
        # note how we are doing a pre order serializer, this is important as it would be linked to the deserializer
        
        self.serial.append(root.val)
        self.serialize_rec(root.left)
        self.serialize_rec(root.right)
        return self.serial
    
    def deserialize_rec(self, data):
        if self.idx >= self.n:
            return
        
        if data[self.idx] == None:
            self.idx +=1
            return None
        
        # note how the deserializer also does a pre-order construction, same as serializer
        # note that pre-order is convenient, as first element of array is root
        # if we did postorder, then we would have to start from the other side 'LRN',
        # worse if we did inorder, we will need to figure out where to start and we cant increment index simply to get left/right subtree
        root = TreeNode(data[self.idx])
        
        self.idx +=1
        root.left = self.deserialize_rec(data)
        root.right = self.deserialize_rec(data)
        return root
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        self.serialize_rec(root)
        return str(self.serial)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # data is given as a string list -- so convert to comma separated string
        data = data.strip()
        data = data.replace('[', '')
        data = data.replace(']', '')        
        data = data.replace(' ', '')
        # now convert sanitized input to list
        data = data.split(',')
        data = [x if x != 'None' else None for x in data]
        self.n = len(data)
        return self.deserialize_rec(data)
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))