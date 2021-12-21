# https://codefights.com/interview-practice/task/rMe9ypPJkXgk3MHhZ
import itertools
from collections import defaultdict

def possibleSums2(coins, quantity):
    sum_set = set()
    coins_dict = defaultdict(int)
    list_coins = []
    i = 0
    for c in coins:
        qty = quantity[i]
        coins_dict[c] = coins_dict[c] + qty
        i = i + 1

    for k, v in coins_dict.items():
        x = [k for i in range(0, v)]
        list_coins = list_coins + x

    for L in range(1, len(list_coins) + 1):
        for subset in itertools.combinations(list_coins, L):
            sum_set.add(sum(subset))

    print(len(sum_set))
    return len(sum_set)

# from stack overflow: https://stackoverflow.com/questions/43642133/complete-search-algorithm-for-combinations-of-coins
# Insanely simple solution: https://www.youtube.com/watch?v=PafJOaMzstY

def possibleSums(coins, quantity):
    maximum = sum((map(lambda t: t[0] * t[1], zip(coins, quantity))))

    dp = [False] * (maximum + 1)
    dp[0] = True
    for coin,q in zip(coins,quantity):
        for b in range(coin):
            num = -1
            for i in range(b,maximum+1,coin):
                if dp[i]:
                    num = 0
                elif num>=0:
                    num += 1
                dp[i] = 0 <= num <= q

    print(sum(dp) - 1)

# from stack overflow: https://stackoverflow.com/questions/43642133/complete-search-algorithm-for-combinations-of-coins
# Implemented 2nd suggested answer here myself

def possibleSums3(coins, quantity):
    result = set()
    result.add(0)
    zipped = list(zip(coins, quantity))
    for c, q in zipped:
        candidates = []
        for j in range(q + 1):
            candidates.append(j * c)

        temp = set()
        # Add candidates to existing elements
        for i in result:
            for k in candidates:
                temp.add(i + k)
        result.update(temp)
    return len(result) - 1



# possibleSums([3, 1, 1], [111, 84, 104])
# possibleSums([1, 2, 3], [2, 3, 10000])
# possibleSums([10, 50, 100], [1, 2, 1])
# possibleSums3([1, 2, 3], [1, 2, 2])
possibleSums3([1, 2], [5000, 2]);
# possibleSums2([1, 2], [5000, 2]);