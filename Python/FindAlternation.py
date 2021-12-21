# from EPI, section 5.8
def alternation(arr):
    lenarr = len(arr)
    if lenarr <=2:
        print(arr)
        return
    arr.sort()
    i = 0
    res = []
    mid = int(lenarr/2)
    if lenarr % 2 == 1:
        j = mid + 1
    else:
        j = mid

    while i < mid and j < lenarr:
        res.append(arr[i])
        res.append(arr[j])
        i +=1
        j +=1

    if lenarr % 2 == 1:
        res.append(arr[mid])

    print(res)

alternation([1])
alternation([1,2])
alternation([1,3,2])
alternation([1,3,2,4,5])
alternation([1,3,2,4,5,6,7,8,9])
