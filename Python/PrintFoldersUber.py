'''
Given list of folders, print the path of a given folder from root. 
If there is no path to the root folder then return an empty string. 
Root level folders will have 0 as id. 
The structure of Folder is like this:

class Folder {
   int id;
   List<int> subfolders;
   String name;
}

Ex: 
Solution([Folder(0, [7, 3], "abc"), Folder(0, [11], "xyz"), Folder(3, [100], "pqr"), 
Folder(8, [], "def"), Folder(7, [9], "ijk"), Folder(9, [], "lmn"), Folder(11,[],"ijk"), 
Folder(100, [], "pqrs")])

Clarification: There can be multiple root level folders. All other folders have unique ids.
Note: printPath method may be called multiple times. Design your solution taking that into account
'''
class Folder:
    def __init__(self, idx, subfolders, name):
        self.idx = idx
        self.subfolders = subfolders
        self.name = name
        self.sub = dict()

class Solution():
    def __init__(self, folderList):
        # parents holds the folders with ID 0
        self.parents = []
        # non parents holds the folders with non 0 ID
        self.nonparents = dict()

        for f in folderList:
            if f.idx == 0:
                self.parents.append(f)
            else:
                self.nonparents[f.idx] = f
        
        # construct the folder relationships
        self.buildFolderPaths(self.parents)
    
    def buildFolderPaths(self, parents):
        for f in parents:
            childList = []
            for ff in f.subfolders:
                child = self.nonparents[ff]
                f.sub[ff] = child
                childList.append(child)
            
            self.buildFolderPaths(childList)
        
        
    def printPath(self, num):
        if num == 0:
            return ""

        self.res = []
            
        def dfs(node, num, path):
            if node.idx == num:
                self.res = path + [self.nonparents[num].name]
                return
            
            for ff in node.sub.values():
                dfs(ff, num, path + [node.name])


        # the folder with id num can be in any of the parents
        # so we need to call dfs on each of them
        for f in self.parents:
            dfs(f, num, [])
        
        return self.res

s = Solution([Folder(0, [7, 3], "abc"), Folder(0, [11], "xyz"), 
Folder(3, [100], "pqr"), Folder(8, [], "def"), Folder(7, [9], "ijk"), 
Folder(9, [], "lmn"), Folder(11,[],"ijk"), Folder(100, [], "pqrs")])

print(s.printPath(9))
print(s.printPath(11))
print(s.printPath(7))
print(s.printPath(3))
print(s.printPath(100))