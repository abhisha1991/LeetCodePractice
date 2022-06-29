# https://leetcode.com/problems/friends-of-appropriate-ages
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        count = 0
        # age[y] > age[x] - already a condition
        # thus means age[y] > 100 and age[x] < 100 is a redundant condition since it is covered by above
        for i in range(len(ages)):
            age = ages[i]
            lower = bisect.bisect(ages, age/2 + 7)
            upper = bisect.bisect(ages, age)
            # the -1 is to not send a friend request to yourself
            count += max(upper-lower-1, 0)
        return count