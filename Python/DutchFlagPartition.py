# section 5.1 from the EPI book
def dutchFlagPartition(arr, pivot):
    smaller = 0
    larger = len(arr) - 1
    for i in range(len(arr)):
        if arr[i] < pivot:
            arr[i], arr[smaller] = arr[smaller], arr[i]
            smaller +=1
    
    for j in range(len(arr) - 1, 0, -1):
        if arr[j] > pivot:
            arr[j], arr[larger] = arr[larger], arr[j]
            larger -=1
        # this condition is important for early exit, else you will do n traversals
        # why are we doing this? because beyond this first j we encounter, every j up till 0 will be less than pivot
        # why? because of the first loop
        if arr[j] < pivot:
            break
    
    print("for pivot {} the array is {}".format(pivot, arr))
    return arr


dutchFlagPartition([0,1,2,0,2,1,0,1], 1)
dutchFlagPartition([0,1,2,0,2,1,0,1], 0)
dutchFlagPartition([0,1,2,0,2,1,0,1], 2)
dutchFlagPartition([0,1,2,0,2,1,1], 0)
dutchFlagPartition([0,1,2,0,2,1,1], 2)