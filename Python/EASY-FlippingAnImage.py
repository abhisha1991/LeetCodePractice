#https://leetcode.com/problems/flipping-an-image/

def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    new_lst=[]
    for lst in A:
        new_lst.append([0 if x==1 else 1 for x in lst[::-1]])
    return new_lst
