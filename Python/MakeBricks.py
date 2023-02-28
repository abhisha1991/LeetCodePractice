'''
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
Return True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops.

make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
'''

def make_bricks(small, big, goal):
    
    big_needed = goal / 5
    goal -= min(big_needed, big) * 5
    if goal <= small:
      return True
    
    return False

'''
The time complexity of this program is O(1) because it only performs a constant number of operations that do not depend on the input size.
The program consists of simple arithmetic operations, comparisons, and a few conditional statements that execute in constant time.
The space complexity of this program is also O(1) because it does not create any data structures that depend on the input size.
Instead, it uses a few variables to store the input values and intermediate results, such as the number of big bricks needed and the remaining goal.
Overall, this program is efficient in terms of both time and space complexity. The arithmetic operations and conditional statements
are straightforward and easy to understand, and the program executes quickly for any input size.
'''
