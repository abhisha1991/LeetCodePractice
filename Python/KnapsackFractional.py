# http://www.geeksforgeeks.org/fractional-knapsack-problem/
# Check out important message below!!!
'''
import operator
stats = {'a':1000, 'b':3000, 'c': 100}
print(max(stats.items(), key=operator.itemgetter(1)))
# For printing the k,v pair with the max value
# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
'''

def frac_knapsack(n, w, vals, wts):
    '''
    n = 3
    w = 50
    vals =     60 100 120
    wts =      10 20  30
    val_wt =   6  5   4
    '''
    result = 0
    if n == 0 or w == 0:
        return result
    val_wt = dict()
    for i in range(0, n):
        val_wt[i] = vals[i] / wts[i]

    while w > 0 and len(val_wt.items()) > 0:
        k, v = get_max_kv(val_wt)
        wt = wts[k]
        if w >= wt:
            w = w - wt
            result += vals[k]
            del val_wt[k]
        else:
            result += val_wt[k] * w
            w = 0

    # IMPORTANT -- HOW TO ROUND A RESULT!!!!
    return round(result, 2)


def get_max_kv(dic):
    maxv = 0
    maxk = 0
    for k, v in dic.items():
        if v > maxv:
            maxv = v
            maxk = k
    return maxk, maxv


t = int(input().strip())
for tt in range(0, t):
    nw = [int(x) for x in input().strip().split(' ')]
    n = nw[0]
    w = nw[1]
    vals = []
    wts = []
    val_wt = [int(x) for x in input().strip().split(' ')]
    for idx, i in enumerate(val_wt):
        if idx % 2 == 0:
            vals.append(i)
        else:
            wts.append(i)

    print(frac_knapsack(n, w, vals, wts))

