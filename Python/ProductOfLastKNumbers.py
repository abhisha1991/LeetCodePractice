# https://leetcode.com/problems/product-of-the-last-k-numbers/
class ProductOfNumbers:
    def __init__(self):
        # we maintain a prefix product array
        # initialize with 1 which is a neutral 
        self.prefix = [1]

    def add(self, num: int) -> None:
        # the main thing to set here is for the case when num = 0
        # we need to reset the prefix array back to 1
        if num == 0:
            # this piece is important because this means that all prefix products
            # have been invalidated
            self.prefix = [1]
        else:
            # prefix is holding the product so far
            last = self.prefix[-1]
            self.prefix.append(last * num)

    def getProduct(self, k: int) -> int:
        n = len(self.prefix)
        if k >= n:
            return 0
        
        # return int otherwise we return float which violates answer
        # this is saying, get the product of all elements so far (last)
        # divide this by product at n-k-1, which is the kth element from last
        # so this will be product of last k elements
        return int(self.prefix[-1]/self.prefix[n-k-1])
            


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)