# section 5.2 of the EPI book - increasing a number by 1 
def incrementInt(arr):
    i = len(arr)-1
    if i < 0:
        return arr
    
    return inc(arr, i)

def inc(arr, i):
    # this is for the case where arr is 99, so we'll need to insert a 3rd element, 1 at index 0, hence returning 100
    if i == -1 and arr[i+1] == 0:
        arr.insert(0, 1)
        return arr
    # if you've reached the first digit
    elif i == -1:
        return arr
    # add the carry from the previous digit
    arr[i] += 1
    # if the digit is less than 10 itself, then we dont need to go more left, so return
    if arr[i] < 10:
        return arr
    # else the digit is equal to 10, ie, 9+1 = 10, so make the num as 0 and move left with the carry by calling inc(i-1)    arr[i] = 0
    return inc(arr, i-1)

print(incrementInt([1,2,8]))
print(incrementInt([1,2,9]))
print(incrementInt([1,9,9]))
print(incrementInt([9,9,9]))
print(incrementInt([9,9,9,9,9,9,9,9,9,9,9,9]))
print(incrementInt([8,9,9,9,9,9]))
print(incrementInt([8,9]))
print(incrementInt([9,9]))
print(incrementInt([9,1,9]))
print(incrementInt([]))
print(incrementInt([9]))