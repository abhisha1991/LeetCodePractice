# https://leetcode.com/problems/find-duplicate-file-in-system/submissions/
import re
from collections import defaultdict

class Solution(object):
    def __init__(self):
        self.dic = defaultdict(list)
        self.res = []
        
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        for i in paths:
            f = i.split()
            root = f[0]
            for j in range(len(f)):
                if j == 0:
                    continue
                file_with_content = f[j]
                content = re.search("\([\w]+\)", file_with_content)
                fname = re.search("[\w]+.txt", file_with_content)
                self.dic[content.group(0)].append("".join([root, "/", fname.group(0)]))
        
                
        for x in self.dic.keys():
            if len(self.dic[x]) > 1:
                self.res.append(self.dic[x])
        return self.res
