# https://www.youtube.com/watch?v=GmpyAMpjpUY
# the above has an excellent explanation to use minheap
# we will try the approach used in MeetingRooms.py, followed by above heap solution

# my approach is below - wont work for an example like [[1,2],[2,3]]. 
# This will say 2 meeting rooms are needed, whereas we need 1
import sys
def getNumMeetingRooms(arr):
    if len(arr) < 2:
        return len(arr)
    
    maxtime = 0
    mintime = sys.maxsize
    for meet in arr:
        maxtime = max(maxtime, meet[1])
        mintime = min(mintime, meet[0])

    maxcount = 0
    for i in range(mintime, maxtime+1):
        count = 0
        for meet in arr:
            if meet[0] <= i <= meet[1]:
                count +=1
        if count > maxcount:
            maxcount = count
    return maxcount

# print(getNumMeetingRooms([[1,2],[2,3]]))

# implementation of min heap solution
import heapq
def getMinMeetingRooms(arr):
    if len(arr) == 0:
        return 0
    
    # sort on the start times
    arr.sort(key = lambda x: x[0])
    # put the first element's end time in the heap. We're making a min heap of the end timings.
    # first element, is the smallest start time as we have sorted the heap
    # note that heapify takes an iterable, hence the outside []
    minheap = [arr[0][1]]
    heapq.heapify(minheap)
    for i in range(1, len(arr)):
        # if start time of current meeting is more than end time of earliest meeting
        if arr[i][0] >= heapq.nsmallest(1, minheap)[0]: # why [0] for nsmallest? because it returns a list
            # get rid off earliest meeting, and add current meeting's end time to heap
            heapq.heappop(minheap)
            heapq.heappush(minheap, arr[i][1])
        else:
            # if there is overlap between current meeting and earliest meeting's end time, book a new room
            # booking a new room = adding to the heap
            # why check earliest meeting? because if there is overlap with earliest meeting's end time, there will be overlap with all other meeting's end time
            heapq.heappush(minheap, arr[i][1])
    print("for input {0} ans is {1}. Minheap is {2}".format(arr, len(minheap), minheap))
    return len(minheap)

getMinMeetingRooms([[1,2],[2,3]])
getMinMeetingRooms([[1,2],[3,4],[2,3]])
getMinMeetingRooms([[8,10],[1,5],[4,6],[1,10]])



