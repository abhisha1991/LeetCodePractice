# https://leetcode.com/problems/group-anagrams/description/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        for i in strs:
            # 2 words belong to the same group if their sorted versions are equal
            si = str(sorted(i))
            if si in dic:
                dic[si].append(i)
            else:
                dic[si] = [i]
        
        return [v for k,v in dic.items()]