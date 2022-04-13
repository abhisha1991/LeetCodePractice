# https://leetcode.com/problems/count-binary-substrings/
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        
        # groups represents a consecutive count of 1s or 0s
        # for example, 00111001 will be [2, 3, 2, 1]
        groups = []
        
        # char at first index
        c = s[0]
        
        # index for s
        i = 1
        
        # number of consecutive 0s and 1s to be put inside the group array
        # g is the current group count
        # set to 1 since we have included s[0]
        g = 1
        
        # create the groups array
        while i < len(s):
            if s[i] == c:
                g +=1
            else:
                groups.append(g)
                # change c to be the other "breaking" character
                # if c was '1' earlier, now it is '0' (and vice versa)
                c = s[i]
                # reset g to be 1
                g = 1
            
            i +=1
        
        # dont forget to add last group!
        groups.append(g)
        
        # what is the below doing? see theory here: https://www.youtube.com/watch?v=MGPHPadxhtQ
        # but at a high level, say groups = [2, 3]
        # this means we have either 00111 or 11000 (exact pos of 1/0 doesnt matter)
        # in either of these, how many binary substrings can we form?
        # say, we take 00111 ==> 01, 0011, ie, 2, which is min(count(0), count(1)) = min(2,3)
        # this above point is the crux of the algo!
        # if we had ten 1s and two 0s, we can still only form 2 binary substrings - 01, 0011
        # which is min(count(0), count(1)) = min(2, 10) = 2
        # this is of course, because the limiting factor is the number of 0s, thus we take min!
        
        # now traverse through groups arr in pairs and take min of the pair
        i = 0
        j = 1
        res = 0
        while j < len(groups):
            res += min(groups[i], groups[j])
            i +=1
            j +=1
        return res