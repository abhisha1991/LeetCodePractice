# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # if everything is negative, return max 
        if all([i < 0 for i in arr]):
            return max(arr)
        
        # at least 1 positive exists in arr
        ignore = 0
        notIgnore = 0
        ans = arr[0]
        
        for n in arr:
            # if number is positive
            # then add to both ignore and notIgnore
            # be as greedy as possible
            if n >= 0:
                ignore +=n
                notIgnore +=n
            else:
                # for ignore, we can either add the current element "n" to our ignore value (dont skip cur val)
                # or we can choose the notIgnore, ie, don't add "n" (ie, skip current val)
                # in other words, take all previous values so far into account except curr element "n"
                # notice that we are only changing notIgnore AFTER USING IT in ignore
                ignore = max(ignore + n, notIgnore)
                # if number is negative, then we must add to notIgnore (by definition of what it means)
                notIgnore += n
            
            # ans is always greedy, so choose max
            ans = max(ignore, notIgnore, ans)
            
            # if ignore or notIgnore are < 0, we always set to 0
            # why? because a subset of arr with 1 element (positive val) has already been (or will be) stored in ans
            # so worst case, we wont contribute anything from our ignore/notIgnore "subset sum", but best case, we'll contribute something positive
            ignore = max(0, ignore)
            notIgnore = max(0, notIgnore)
        return ans