# http://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/
# sort the array then pick the last k elements
# Time complexity is O(n logn) + O(k)
def k_largest_elements_method1(arr, k):
    arr.sort()
    lenarr = len(arr)
    i = lenarr - 1
    result = []
    while i >= lenarr - k:
        result.append(arr[i])
        i -= 1

    return result

# uses bubble sort, capped at k times, time complexity is O(nk)
def k_largest_elements_method2(arr, k):
    result = []
    i = 0
    while i < k:
        j = i + 1
        while j < len(arr):
            if arr[i] < arr[j]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
            j += 1
        result.append(arr[i])
        i += 1

    return result

# Third method is as follows
'''
1) Build a Max Heap tree in O(n)
2) Use Extract Max k times to get k maximum elements from the Max Heap O(klogn)
Time complexity: O(n + klogn)
'''

# Fourth method is as follows
'''
1) Build a Min Heap MH of the first k elements (arr[0] to arr[k-1]) of the given array. O(k)

2) For each element, after the kth element (arr[k] to arr[n-1]), compare it with root of MH.
a) If the element is greater than the root then make it root and call heapify for MH
b) Else ignore it.
// The step 2 is O((n-k)*logk)

3) Finally, MH has k largest elements and root of the MH is the kth largest element. 
Why? Because in 2.a and 2.b you eliminated the n-k small elements, either by ignoring or by replacing

Time Complexity: O(k + (n-k)Logk) without sorted output. If sorted output is needed then O(k + (n-k)Logk + kLogk)
'''

t = int(input())
for i in range(t):
    nk = [int(x) for x in input().strip().split(' ')]
    arr = [int(x) for x in input().strip().split(' ')]
    result = k_largest_elements_method1(arr, nk[1])
    ans = ''
    for i in result:
        ans += str(i) + ' '
    print(ans)

