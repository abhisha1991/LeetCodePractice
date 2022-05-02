# https://leetcode.com/problems/design-file-system
class FileSystem:

    def __init__(self):
        self.dic = dict()

    def createPath(self, path: str, value: int) -> bool:
        # if path is like /a/b/c
        if path.count('/') > 1:
            dirs = path.split('/')
            l = len(dirs)
            # get everything before the last /, ie, dirs now is ['a','b']
            dirs = dirs[:l-1]
            
            tmp = '/'
            for d in dirs:
                tmp += d + '/'
                
            tmp = tmp.strip('/')
            tmp = '/' + tmp
            # tmp now is /a/b
            # we are basically checking if parent path (/a/b) is registered or not for path (/a/b/c) 
            if tmp not in self.dic:
                return False
        
        if path not in self.dic:
            self.dic[path] = value
            return True
        return False

    def get(self, path: str) -> int:
        if path in self.dic:
            return self.dic[path]
        return -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)