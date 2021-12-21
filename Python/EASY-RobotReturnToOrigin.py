#https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves.count('R')==moves.count('L') and moves.count('U')==moves.count('D'):
            return True
        else:
            return False
