# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # key = int value of node, value = node object itself
        dic = dict()
        
        # key = node object, value = parent object of that node objet
        parent = dict()
        
        if not root:
            return []

        def dfs(node, p):
            if not node:
                return
            
            # create the 2 dictionaries doing a dfs of the tree
            dic[node.val] = node
            parent[node] = p
            
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, root)
        
        # go through all delete values
        for d in to_delete:
            # get the node ref from the int key 'd'
            n = dic[d]
            
            # get the parent node of node 'n'
            p = parent[n]
            
            # if the parent's left link was node 'n', then cut that connection from parent to n
            if p.left == n:
                p.left = None
                
            # if the parent's right link was node 'n', then cut that connection from parent to n    
            elif p.right == n:
                p.right = None
            
            # make the left/right links of "node to delete" also as None
            n.left = None
            n.right = None
            
            # delete that node from dictionary
            del dic[d]
        
        res = []
        '''
        this part is important
        imagine if your tree was 
                             1
                           /   \
                          2     3
                         / \   / \
                        4   5 6   7
        
        and values to delete are 3,5
        then we want to return [1, 6, 7] -- ie, these 3 sub trees after deleting nodes 3,5
        
        dic after the above steps will contain values as nodes [1, 2, 4, 6, 7]
        now we notice that sub trees of node 2 and node 4 are just child sub trees of  1, ie, child of node 1
                                                                                      /
                                                                                     2
                                                                                    /
                                                                                   4
                                                                                   
        so we need a way to de-dupe the dictionary values, ie, we want to avoid adding sub tree 2,4 in ans
        this is what the below code does
        '''
        
        for val, node in dic.items():
            # CASE 1
            # consider dictionary item sub tree 6
            # its parent node is 3, ie, one of the values to be deleted
            # notice how it will hit the first if condition (if p.val in to_delete)
            # thus we end up adding 6 to result


            # CASE 2
            # consider dictionary item sub tree 1
            # its parent node is 1, ie, the node itself
            # notice how it will hit the second if condition (elif p.val == node.val)
            # thus we end up adding 1 to result
            
            # CASE 3
            # consider dictionary item sub tree 2
            # its parent will be node 1
            # notice how neither of the 2 below conditions will be met for node 2
            # so we won't add sub tree with node 2 to res
            # same argument can be made for sub tree 4
            
            p = parent[node]
            
            if p.val in to_delete:
                res.append(node)
                
            elif p.val == node.val:
                    res.append(node)
        
        return res