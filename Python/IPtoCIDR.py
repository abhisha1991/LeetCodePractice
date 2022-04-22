# https://leetcode.com/problems/ip-to-cidr/
from math import log2
class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        def ip_to_num(ip):
            numbers = list(map(int, ip.split(".")))
            print(f"ip2num parts are {(numbers[0] << 24)}, {(numbers[1] << 16)}, {(numbers[2] << 8)}, {numbers[3]}")
            
            n = (numbers[0] << 24) + (numbers[1] << 16) + (numbers[2] << 8) + numbers[3]
            return n

        def num_to_ip(num):
            mask = 255
            print(f"num2ip parts are {num >> 24}, {(num >> 16) & mask}, {(num >> 8) & mask}, {num & mask}")
            return f'{num >> 24}.{(num >> 16) & mask}.{(num >> 8) & mask}.{num & mask}'
        
        res = []
        num = ip_to_num(ip)
        
        # while we still have addresses to cover
        while n > 0:
            if num == 0:
                low_bit = 1 << 32
            else:
                # consider 10 -- which is 01010 in binary
                # negative 10 will be 2s complement and add 1 ie, 10110
                # now if we 'and' these 2 numbers 01010 and 10110 -- 00010
                # this states that in the number 10, the lowest 1 bit is at index 2nd last
                # https://stackoverflow.com/questions/12247186/find-the-lowest-set-bit
                low_bit = num & (-num)

            # find the largest low bit you can get 
            # so while this low bit is larger than n, we need to keep decrementing it with right shift
            # since we cant claim IP addresses larger than remaining capacity
            while low_bit > n:
                low_bit >>= 1
                
            # finally low bit is less than n, so we can claim these many IPs
            n -= low_bit
            res.append(f'{num_to_ip(num)}/{32 - int(log2(low_bit))}')
            num += low_bit
        return res