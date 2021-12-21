# given an array, place all even numbers before odd numbers
# do this in constant space. From EPI book section 5.1
def evenBeforeOdd(arr):
    j = len(arr)-1
    if j < 1:
        return arr
    i = 0
    # i looks for odd number starting from the beginning of the array
    # j looks for even number starting from end of array
    # when you find such a pair, swap the 2 elements
    odd = False # indicates whether we have found an odd number
    even = False # indicates whether we have found an even number
    while i < j:
        if not odd and arr[i] % 2 == 1:
            odd = True
        
        if not even and arr[j] % 2 == 0:
            even = True
        
        if odd and even:
            # we have found a pair, so do the swapping
            arr[i], arr[j] = arr[j], arr[i]
            # reset odd and even
            odd = even = False

        if not odd:
            i +=1
        if not even:
            j -=1
    
    print(arr)
    return arr


evenBeforeOdd([1,2,3,4,5,6,7,8])
evenBeforeOdd([1,3,5,7,9])
evenBeforeOdd([2,4,6,8,10])
