# https://www.youtube.com/watch?v=s6FhG--P7z0&t=256s
# http://www.geeksforgeeks.org/dynamic-programming-set-18-partition-problem/


def subset_sum_problem(n, nums):
    if sum(nums) % 2 == 1:
        return "NO"
    temp = int(sum(nums) / 2) + 1
    ss_list = []
    '''
        0 1 2 3 4 5 6
      1 T T F F F F F
      3 T T F 
      3 T
      5 T
    '''
    for i in range(len(nums)):
        ls = [None] * temp
        ss_list.append(ls)

    for i in range(len(nums)):
        for j in range(temp):
            if j == 0:
                ss_list[i][j] = "YES"
                continue

            if i == 0 and ss_list[i][j] == None:
                if nums[i] == j:
                    ss_list[i][j] = "YES"
                else:
                    ss_list[i][j] = "NO"
                continue

            if nums[i] > j:
                ss_list[i][j] = ss_list[i - 1][j]

            if nums[i] <= j:
                # you dont include nums[i], take the value from above column
                ans1 = ss_list[i - 1][j]
                # you do include nums[i], so you subtract nums[i] from j and look above
                ans2 = ss_list[i - 1][j - nums[i]]
                if ans1 == "YES" or ans2 == "YES":
                    ans = "YES"
                else:
                    ans = "NO"
                ss_list[i][j] = ans

    return ss_list[len(nums) - 1][temp - 1]


print(subset_sum_problem(4, [1, 3, 3, 5]))
x = [87, 56, 43, 91, 27, 65, 59, 36, 32, 51, 37, 28, 75, 7, 74]
print(subset_sum_problem(len(x), x))
x = [858, 395, 29, 237, 235, 793, 818, 428, 143, 11, 928, 529, 776, 404, 443, 763, 613, 538, 606, 840, 904, 818]
print(subset_sum_problem(len(x), x))
'''
t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    nums = [int(x) for x in input().strip().split(' ')]
    print(subset_sum_problem(n, nums))
'''