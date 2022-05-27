# https://leetcode.com/problems/detect-squares/
from collections import defaultdict
class DetectSquares:

    def __init__(self):
        self.dic = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.dic[(point[0], point[1])] +=1
        
    def count(self, point: List[int]) -> int:
        x1, y1 = point
        count = 0
        # find diagonal point
        '''
            consider
            
            case 1                                       case 3
                     *(x1,y1)                                  *(x1,y1)
            
            
              *                                                            *
              (x3,y3)                                                      (x3,y3)
              
                                           or
             
             case 2                                      case 4    
                     *(x3,y3)                                   *(x1,y1)
            
            
              *                                                             *
              (x1,y1)                                                       (x3,y3)
            
            in each of these diagonal situations, abs(x1-x3) == abs(y1-y3) 
            and these are separate points, ie, x1 != x3
        '''
        for x3, y3 in self.dic.keys():
            if abs(x1-x3) == abs(y1-y3) and x1 != x3:
                ans = 1 * self.dic[(x3,y3)]
                # for all 4 cases above, these are the 2 remaining points
                if (x3, y1) in self.dic and (x1, y3) in self.dic:
                    ans = ans * self.dic[(x3, y1)] * self.dic[(x1, y3)]
                    count += ans
                
        return count


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)