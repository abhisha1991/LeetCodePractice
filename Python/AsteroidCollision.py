# https://leetcode.com/problems/asteroid-collision
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for i in range(len(asteroids)):
            if not ans:
                ans.append(asteroids[i])
                continue
            
            # no collision, because incoming astroid is in same direction as top of stack
            if asteroids[i] < 0 and ans[-1] < 0:
                ans.append(asteroids[i])
                continue
            
            if asteroids[i] > 0:
                ans.append(asteroids[i])
                continue
            
            residual = None
            # collision is due if directions are opposite
            if asteroids[i] < 0 and ans[-1] > 0:
                while ans and ans[-1] > 0:
                    # find residual of collision
                    residual = ans[-1] + asteroids[i]
                    # top of stack was bigger than incoming asteroid
                    # then destroy incoming asteroid and keep top of stack as is
                    if residual > 0:
                        break
                    else:
                        # incoming asteroid is bigger than (or equal to) top of stack
                        # so remove top of stack asteroid
                        # keep doing this as long as collisions are in favor of incoming asteroid
                        ans.pop()
                        # incoming asteroid and top of stack were equal sized
                        # so break out of while loop
                        if residual == 0:
                            break
                
                # if there was a large incoming asteroid and other asteroids in stack
                # are in same direction as incoming asteroid, 
                # then add this incoming asteroid to stack
                if residual < 0:
                    if ans and ans[-1] < 0:
                        ans.append(asteroids[i])
                    elif not ans:
                        ans.append(asteroids[i])

        return ans