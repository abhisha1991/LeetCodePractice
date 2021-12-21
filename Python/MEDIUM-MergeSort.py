# https://www.youtube.com/watch?v=TzeBrDU-JaY
class Solution(object):
    def __init__(self):
        self.arr = None

    def driver(self, A):
        self.arr = A
        self.mergesort(0, len(A) - 1)
        print(self.arr)
        return self.arr

    def mergesort(self, low, high):
        if low >= high:
            return
        mid = int((low + high)/2)
        self.mergesort(low, mid)
        self.mergesort(mid + 1, high)
        self.merge(low, mid, high)

    def merge(self, low, mid, high):
        aux = [None] * len(self.arr)
        for i in range(low, high + 1):
            aux[i] = self.arr[i]
        i = low
        j = mid + 1
        k = low

        while k <= high and i <= mid and j <= high:
            if aux[i] <= aux[j]:
                # remember arr has index of k
                self.arr[k] = aux[i]
                i += 1
            else:
                # remember arr has index of k
                self.arr[k] = aux[j]
                j += 1
            # k always increases no matter what
            k += 1

        while i <= mid:
            # remember arr has index of k
            self.arr[k] = aux[i]
            i +=1
            # dont forget to increase k
            k +=1

        while j <= high:
            # remember arr has index of k
            self.arr[k] = aux[j]
            j += 1
            # dont forget to increase k
            k += 1

s = Solution()
s.driver([2,4,6,1,3,5,7,3,9,8])