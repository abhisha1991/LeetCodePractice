# https://leetcode.com/problems/design-in-memory-file-system
class Dir:
    def __init__(self):
        # key = directory name (str), value = sub directory object
        self.dirs = dict()
        # dictionary of files at this directory with key = filename, value = file content 
        self.files = dict()
    
class FileSystem:

    def __init__(self):
        self.root = Dir()

    def ls(self, path: str) -> List[str]:
        toReturn = []
            
        if path == '/':
            # get files/directories at the root level, ie, at the '/' level
            toReturn.extend(self.root.files.keys())
            toReturn.extend(self.root.dirs.keys())
            toReturn.sort()
            return toReturn
        
        r = self.root
        d = path.split('/')
        # we know that the path is something like /a/b/c
        # keep going into last but 1 sub directory
        # ie, reach until 'c'
        # we start the iteration from 1, because we are skipping the first '/' in /a/b/c
        for i in range(1, len(d)-1):
            subdirectory = d[i]
            r = r.dirs[subdirectory]
        
        # now we're at the last level of the path, ie, 'c'
        # we need to check if 'c' is a file or a directory
        name = d[len(d)-1]
        
        # if its a file, simply add file name and return
        if name in r.files.keys():
            toReturn.append(name)
        else:
            # 'c' is a directory with possibly files at its level and possibly children directories under it
            
            # add the files under this directory 'c'
            toReturn.extend(r.dirs[name].files.keys())
            
            # add the directory names under this parent directory 'c'
            # ie, go one level down in directory from 'c'
            r = r.dirs[name]
            # add all directory keys that fall under the child of 'c'
            toReturn.extend(r.dirs.keys())
            
        toReturn.sort()
        return toReturn
        

    def mkdir(self, path: str) -> None:
        r = self.root
        d = path.split('/')
        # we get a path like /a/b/c --> we need to keep creating directories till we reach 'c'
        for i in range(1, len(d)):
            subdirectory = d[i]
            if subdirectory not in r.dirs.keys():
                r.dirs[subdirectory] = Dir()
                
            # go to the next level in both cases - 
            # in case you created the sub directory or if it already existed
            r = r.dirs[subdirectory]

    def addContentToFile(self, filePath: str, content: str) -> None:
        d = filePath.split('/')
        r = self.root
        # say path was /a/b/c/filename --> so we need to traverse till sub directory 'c'
        for i in range(1, len(d)-1):
            subdirectory = d[i]
            r = r.dirs[subdirectory]
        
        # now we're at the last level, which is a file
        name = d[len(d)-1]
        
        # if file doesn't exist at this level, create file and add content
        if name not in r.files:
            r.files[name] = content
        else:
            # file does exist
            # so append content
            r.files[name] += content
            
    def readContentFromFile(self, filePath: str) -> str:
        d = filePath.split('/')
        r = self.root
        # say path was /a/b/c/filename --> so we need to traverse till sub directory 'c'
        for i in range(1, len(d)-1):
            subdirectory = d[i]
            r = r.dirs[subdirectory]
        
        # now we're at the last level, which is a file
        name = d[len(d)-1]
        return r.files[name]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)