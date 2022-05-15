# https://leetcode.com/problems/dot-product-of-two-sparse-vectors
class SparseVector:
    def __init__(self, nums: List[int]):
        self.dic = dict()
        for i in range(len(nums)):
            if nums[i] != 0:
                self.dic[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        v1 = self.dic
        v2 = vec.dic
        
        # get the keys as a set
        s1 = set(v1.keys())
        s2 = set(v2.keys())
        
        # get an intersection of the 2 sets since we can only calculate the product if index exists in both
        s3 = s1.intersection(s2)
        total = 0 
        for i in s3:
            total += v1[i] * v2[i]
        return total

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)