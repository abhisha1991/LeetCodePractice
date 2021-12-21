# https://codefights.com/interview-practice/task/njfXsvjRthFKmMwLC
from collections import defaultdict


def containsCloseNums(nums, k):
    indices_of_equal_nos = defaultdict(list)
    for i in range(0, len(nums)):
        key = nums[i]
        indices_of_equal_nos[key].append(i)

    for k1, v in indices_of_equal_nos.items():
        if len(v) <= 1:
            continue
        if len(v) == 2:
            return abs(v[0] - v[1]) <= k
        # There are 3 elements at least in v, we need to take pairs
        else:
            for x in range(0, len(v)):
                for y in range(x + 1, len(v)):
                    if abs(v[x] - v[y]) <= k:
                        return True

    return False

containsCloseNums([1, 0, 1, 1], 1)
containsCloseNums([2, 2], 2)
containsCloseNums([0, 1, 2, 3, 5, 2], 2)
containsCloseNums([1], 1)
containsCloseNums([1, 2, 1], 2)
containsCloseNums([0, 1, 2, 3, 5, 2], 3)