class Solution(object):
    def reverse2(self, x):
        s = int(x > 0)
        if s == 0:
            s = -1 # take the sign of the number
        # multiply sign * integer version of the absolute number reversed without the sign
        n = s * int(str(abs(x))[::-1])
        return n if n.bit_length() < 32 else 0

    def reverse(self, x):
        if x == 0:
            return 0
        neg = False
        if x < 0:
            neg = True
            x = abs(x)
        lx = list()

        while x > 0:
            r = x % 10
            lx.append(r)
            x = int(x / 10)

        while True:
            if 0 == lx[0]:
                lx = lx[1:]
            else:
                break

        rev = int(''.join([str(x) for x in lx]))
        if rev >= (1024 * 1024 * 1024 * 2):
            return 0
        if neg is True:
            return rev * -1
        return rev

s = Solution()
print(s.reverse2(-123))
print(s.reverse2(-5200))
print(s.reverse(-123))
print(s.reverse(-5200))
'''
public int reverse(int x) {
        long rev= 0;
        while( x != 0){
            rev= rev*10 + x % 10;
            x= x/10;
            if( rev > Integer.MAX_VALUE || rev < Integer.MIN_VALUE)
                return 0;
        }
        return (int) rev;
    }
'''