# https://leetcode.com/problems/k-similar-strings
class Solution:                     
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        
        def swap(s, i, j):
            s = list(s)
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            return ''.join(s)
        
        # length will remain const (s1, s2 and others) as the length of any swaps will not affect length
        l = len(s1) 
        dic = dict()
        q = [(s1, 0)]
        
        visited = set()
        visited.add(s1)
        
        # traditionally, to get all 2 letter swaps of a string of length - you can do it in o(n2) time
        # 2 for loops over a string's chars, swap items next to each other, 1 letter apart, 2 letters apart and so on
        # that will be expensive
        def nbors(cur, target):
            nbr = []
            i = 0
            
            # if the characters are the same, then there's no point swapping them
            # consider cur is aaabc and dest is aaacb, there's no point trying to swap any of the first 3 'a' chars 
            while cur[i] == target[i]:
                i +=1
            
            # now i is pointing to the target's index (the point where cur and target differ)
            # define j going from i+1 till the end, j will be cur's index
            for j in range(i+1, l):
                # https://www.youtube.com/watch?v=GacKZ1-p3-0
                # this is the optimization that makes the difference
                '''
                consider 2 strings 
                cur =     a a a a b c d a f a
                                    |
                                    j=5
                                    
                target =  a a a a a f c a d b
                                  |
                                  i=4
                
                we know that chars at i differ, ie, cur[i] != target[i], what we want to do is find 
                another position j in cur, such that cur[j] == target[i], ie, cur[j] == 'a', which is at j=7 and j=9
                why do we want to match cur[j] with target[i]? because we want to make cur as close to target via a swap!
                
                now which j should be chosen? 7 or 9?, if we chose to swap cur[i] with j=7, then we will make a bad
                choice! why? because we will mess up the relation such that target[7] would no longer match cur[7] -
                like they do now! So we don't want to regress!
                
                If we chose to swap cur[i] with cur[9], thats a fine choice because we will satisfy cur[4] == target[4]
                which will become 'a' and additionally, we will make cur[9] == target[9], ie, 'b' - so we will bring
                cur closer to target!
                
                So these are our 2 conditions of choosing swap below!
                '''
                if cur[j] == target[i] and target[j] != cur[j]:
                    t = swap(cur, i, j)
                    nbr.append(t)
                    
            return nbr
            
        # bfs!
        while q and s2 not in dic:
            s, count = q.pop(0)
            
            for t in nbors(s, s2):
                if t not in visited:
                    q.append((t, count+1))
                    dic[t] = count+1
                    if t == s2:
                        return dic[s2]
                    
        return dic[s2]