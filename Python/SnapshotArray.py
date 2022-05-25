# https://leetcode.com/problems/snapshot-array
class SnapshotArray:

    def __init__(self, length: int):
        self.snapId = 0
        self.dic = defaultdict(list)
        for i in range(length):
            self.dic[i] = [(self.snapId, 0)]

    def set(self, index: int, val: int) -> None:
        arr = self.dic[index]
        snap = arr[-1][0]
        if snap == self.snapId:
            self.dic[index].pop()

        self.dic[index].append((self.snapId, val))

    def snap(self) -> int:
        self.snapId +=1
        return self.snapId-1
    
    def get(self, index: int, snap_id: int) -> int:
        arr = self.dic[index]
        low = 0
        high = len(arr)-1
        
        # because we have this sorted by snap number
        # we can do a binary search when getting, instead of linear search
        while low <= high:
            mid = (low + high)//2
            snap = arr[mid][0]
            val = arr[mid][1]
            if snap == snap_id:
                return val
            
            elif snap > snap_id:
                high = mid-1
            else:
                low = mid+1
        
        if mid == 0:
            return arr[mid][1]
        
        if arr[mid-1][0] <= snap_id < arr[mid][0]:
            return arr[mid-1][1]
        
        return arr[mid][1]
        

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)