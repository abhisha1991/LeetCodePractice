# https://leetcode.com/problems/accounts-merge/
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email2Id = dict()
        id2Name = dict()
        graphEmail = defaultdict(list)
        
        for i in range(len(accounts)):
            name = accounts[i][0]
            # connect id to name -- for easy lookup for name later on
            id2Name[i] = name
            emails = accounts[i][1:]
            # connect an id to a representative email, say 1st email in list
            email2Id[emails[0]] = i 
            
            # neighbors are established in bidirectional nature
            # a is neighbor of b and b is neighbor of a
            for e in emails:
                graphEmail[e].extend(emails)
        
        visited = set()
        resDic = defaultdict(list)
        
        def dfs(email):
            visited.add(email)
            self.group.add(email)
            
            for nbor in graphEmail[email]:
                if nbor not in visited:
                    dfs(nbor)
            
        for k,v in graphEmail.items():
            if k not in visited:
                # group contains the group of emails belonging to this dfs run
                # so it needs to be reset to empty set every time
                self.group = set()
                dfs(k)
                
                # after dfs, add the emails in group to result
                for e, idx in email2Id.items():
                    # if representative email is found in the group
                    if e in self.group:
                        name = id2Name[idx]
                        resDic[idx] = [name] + sorted(list(self.group))
                        break
        
        res = []
        for k,v in resDic.items():
            if v not in res:
                res.append(v)
        return res