# https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem
import itertools

# solution 1
steps = [1, 2, 3]
s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    count = 0
    # find permutations of sums of n
    for j in range(1, n + 1):
        result = [p for p in itertools.product(steps, repeat=j)]
        for i in result:
            if sum(i) == n:
                count += 1

    print(count)

# solution 2
'''
public static int calcNum(int n) {
        int[] array = new int[n];
        if (n == 1) {
            return 1;
        }
        else if(n == 2) {
            return 2;
        }
        else if(n == 3) {
            return 4;
        }
        array[0] = 1;
        array[1] = 2;
        array[2] = 4;
        for (int i = 3; i < n; i++) {
            array[i] = array[i-1] + array[i-2] + array[i-3];
        }
        return array[array.length-1];
    }
'''

# solution 3
dict_davis = dict()


def davis(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in dict_davis.keys():
        return dict_davis[n]
    dict_davis[n] = davis(n - 1) + davis(n - 2) + davis(n - 3)
    return dict_davis[n]


steps = [1, 2, 3]
s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    print(davis(n))




