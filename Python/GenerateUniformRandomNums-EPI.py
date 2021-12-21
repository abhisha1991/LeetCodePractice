# generate a number between lower and upper inclusive
# personally, this doesnt seem to be very random as we get skewed distributions
# this comes from section 4.10 from EPI
'''
key: 10 and value 49915
key: 2 and value 6109
key: 3 and value 6364
key: 6 and value 24913
key: 4 and value 12699
'''
import random
from collections import defaultdict
def generateNums(lower, upper):
    while True:
        i = 0
        res = 0
        numrange = upper - lower + 1
        while (1 << i) < numrange:
            r = random.randrange(2) # gives either a 0 or 1
            res = (res << 1) or r
            i +=1

        if res < numrange:
            break
    return res + lower

resdic = defaultdict(int)
for i in range(100000):
    resdic[generateNums(2,10)] +=1

for k,v in resdic.items():
    print("key: {0} and value {1}".format(k,v))