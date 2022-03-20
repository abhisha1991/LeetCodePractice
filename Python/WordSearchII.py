# https://leetcode.com/problems/word-search-ii
class Trie():
    def __init__(self):
        self.isWordEnd = False
        self.children = dict()
        # slight optimization, we have a full word field
        # uses extra memory to store the full word in trie, 
        # but it saves time in the recursive call, rather than passing the
        # word seen so far and updating it in function calls, we just directly have the full word available from the trie itself
        self.fullWord = None
    
    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        
        cur.isWordEnd = True
        cur.fullWord = word
    
    def startswith(self, prefix):
        cur = self
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        visit = set()
        
        rows = len(board)
        cols = len(board[0])
        root = Trie()
        for w in words:
            root.insert(w)
            
        res = set()
        def dfs(r, c, node):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            
            if (r,c) in visit:
                return 
            
            # if char is not in trie
            if board[r][c] not in node.children:
                return
            
            # remember to add visited only after you have found a valid match
            # else you may never remove (r,c) from visited, in which case you'll get weird results
            # since it will prematurely return in the next step of the dfs
            visit.add((r,c))            

            # move down trie
            node = node.children[board[r][c]]
            
            # if we reach end of word, then add to result
            if node.isWordEnd:
                res.add(node.fullWord)
            
            for d in directions:
                dfs(r + d[0], c + d[1], node)
                
            # after visiting all possible paths from current path, cleanup after yourself
            visit.remove((r,c))
        
        
        for r in range(rows):
            for c in range(cols):
                # slight optimization, only if there is a prefix starting with current cell do we proceed ahead,
                # else we would go through every pos of the board
                if root.startswith(board[r][c]):
                    dfs(r, c, root)      
        
        return list(res)