import sys

# needs leetcode premium sub
# https://leetcode.com/problems/meeting-rooms/
def canMeet(arr):
    # arr is a list of start and end times
    # example input: [[0,30],[5,10],[15,20]]
    # here there is overlap that is happening, so a person cannot attend all 3 meetings without overlap
    # so return ans as false

    # another input: [[7,10],[2,4]]
    # return true because person can attend both meetings

    # if there is less than 2 meetings, we can attend the meetings
    if len(arr) < 2:
        print("CAN meet for input {0}".format(arr))
        return True 
    maxtime = 0
    mintime = sys.maxsize
    for meet in arr:
        maxtime = max(maxtime, meet[1])
        mintime = min(mintime, meet[0])

    # i is every minute between mintime and maxtime
    # if at any minute, we are in 2 or more meetings, we return false
    for i in range(mintime, maxtime+1):
        count = 0
        for meet in arr:
            if meet[0] <= i <= meet[1]:
                count +=1
                if count > 1:
                    print("CANNOT meet for input {0}".format(arr))
                    return False
    
    print("CAN meet for input {0}".format(arr))
    return True

# alternate solution would be to do MergeIntervals.py function
# get the length of the stack, if that is lesser in length than the input length, it means we have merged an interval 
# ==> there is overlap, so return false. If the length is the same, return true

canMeet([[0,30],[5,10],[15,20]])
canMeet([[0,30]])
canMeet([])
canMeet([[1,2],[2,3]])
canMeet([[1,2],[3,3]])