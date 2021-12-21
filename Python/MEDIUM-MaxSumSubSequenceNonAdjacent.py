# https://www.youtube.com/watch?v=UtGtF6nc35g&index=34&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr

def maxsumNonAdj(arr):
    inclusive = arr[0]
    exclusive = 0

    for i in range(1, len(arr)):
        temp = inclusive
        inclusive = max([inclusive, exclusive + arr[i]])
        exclusive = temp

    print(max([inclusive, exclusive]))

maxsumNonAdj([4,1,1,4,2,1])
maxsumNonAdj([1,2,3,4,5,6,7,8,9]) # sum of all odd nums
maxsumNonAdj([1,2,3,4,5,6,7,8,9,10]) # sum of all even nums