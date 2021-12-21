# section 5.5 of the EPI book
# delete duplicate elements from a sorted array
def deletedupes(arr):
    if len(arr) == 0:
        return arr

    print("input is {}".format(arr))
    # think of end as the index before which (ie, till end-1) you have everything sorted out
    # ie, this is the index, before which everything is distinct
    # this index only increments if the elements encountered by index i are different
    end = 1
    for i in range(1, len(arr)):
        if arr[end-1] != arr[i]:
            arr[end] = arr[i]
            end +=1

    print("output is {}".format(arr[:end]))
    return arr[:end]


(deletedupes([1,2,2,2,2,3,4,4,4,5,6,7,7]))
(deletedupes([1,2,2]))
(deletedupes([1,1,1,1,1]))