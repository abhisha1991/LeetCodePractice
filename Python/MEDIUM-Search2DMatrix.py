class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m is 0:
            return False
        n = len(matrix[0])
        # if we have a 3 x 1000 matrix, then it would make sense to do bin search on array of 1000, so that your
        # worst case time complexity is 3 log 1000
        if m <= n:
            for i in matrix:
                print("searching in array", i)
                if self.binsearch(target, i, 0, n - 1):
                    return True
        else:
            # if we have a 1000 x 3 matrix, then do bin search 3 times for each column matrix of 1000
            # so that time complexity is 3 log 1000 vs 1000 log 3
            j = 0
            while j < n:
                temp = []
                for i in matrix:
                    temp.append(i[j])
                print("searching in array", temp)
                if self.binsearch(target, temp, 0, m - 1):
                    return True
                j += 1
        return False

    # basic binary search
    def binsearch(self, target, nums, lo, hi):
        if lo <= hi:

            mid = int((lo + hi) / 2)
            print("mid is", mid)
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                return self.binsearch(target, nums, lo, mid - 1)
            else:
                return self.binsearch(target, nums, mid + 1, hi)

        return False