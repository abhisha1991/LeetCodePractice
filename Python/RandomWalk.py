import random
class Solution(object):
    def random_walk(self, n):
        x = 0
        y = 0
        for i in range(n):
            (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            x += dx
            y += dy

        return x, y

    def main_walk(self, num_walks, n):
        count = 0
        # we decide to do many walks, caught in num_walks
        for i in range(num_walks):
            # each walk size is n
            x, y = self.random_walk(n)
            if abs(x) + abs(y) <= 4:
                count += 1

        return float(count/num_walks) * 100

# vary walk size from 1 to 30
s = Solution()
for i in range(1, 31):
    num_walk = 10000
    count = s.main_walk(num_walk, i)
    print("For a walk of size {0} and doing {1} simulations for this size, we get {2} % of walks are less than 4".format(i, num_walk, count))