# https://leetcode.com/problems/race-car/
class Solution:
    # both time and space complexity are log2(t) where t is target
    def racecar(self, target: int) -> int:
        
        def updatePos(instruction, p, s):
            if instruction == 'A':
                p += s
            return p
        
        def updateSpeed(instruction, s):
            if instruction == 'A':
                s = s * 2
            else:
                if s > 0:
                    s = -1
                else:
                    s = 1
            return s
        
        # q elements are (pos, speed, pathCount, instruction)
        q = [(0, 1, 0, 'A')]
        pos = q[0][0]
        visited = set()
        
        while q:
            pos, speed, pathCount, instruction = q.pop(0)

            if pos == target:
                return pathCount
            
            if (pos, speed, instruction) in visited:
                continue
            
            visited.add((pos, speed, instruction))
            p = updatePos(instruction, pos, speed)
            s = updateSpeed(instruction, speed)
            
            # always move forward as an option
            # if new position 'p' is less than or equal to target, or even greater than target
            q.append((p, s, pathCount+1, 'A'))    
            
            # however, move backward, when:
            # 1. the new pos (p+s) will overshoot the target and we're moving with +ve speed
            # 2. the new pos (p+s) will be less than target and we are on -ve speed, ie, moving further away left from the target
            '''
                    case 1:
                                T  pos   -(speed)->

                    case 2:     
                            <-(speed)-   pos   T

            '''
            if (p + s > target and s > 0) or (p + s < target and s < 0):
                q.append((p, s, pathCount+1, 'R'))
        
        return sys.maxsize