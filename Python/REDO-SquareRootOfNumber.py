# This uses newtonian method
# There is an alternate way using Binary search, however, that doesnt give the correct answer
# - it gives nearest smallest integer as square root
'''
public int mySqrt(int x)
{
    int left = 1, right = x;
    while (left <= right)
    {
        // NOTE WE NEED TO TYPECAST MID TO INT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        int mid = (left + right) / 2;
        // The below condition is same as mid * mid == x
        // Writing like this to avoid overflow, mid * mid may lead to overflow
        // x/mid will NEVER lead to overflow
        if (mid == x / mid)
        {
            return mid;
        }
        // The below condition is same as mid * mid > x
        // Writing like this to avoid overflow, mid * mid may lead to overflow
        // x/mid will NEVER lead to overflow
        else if (mid < x / mid)
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }
    return right;
}
'''
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r * r > x:
            prev_r = r
            # The idea behind this is simple
            # https://www.youtube.com/watch?v=cOmAk82cr9M
            r = (r + x / r) / 2
            # this is done to avoid it from going into infinite loop, try removing this and doing sqrt(5)
            if prev_r == r:
                break
        return r


s = Solution()
print(s.mySqrt(5))
