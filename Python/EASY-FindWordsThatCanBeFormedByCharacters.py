#https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_dic = dict()
        tot=0
        char_dic = Counter(chars)
        for word in words:
            count = 0
            for ch in word:
                check = True
                if ch not in char_dic.keys():
                    check = False
                    break
                elif word.count(ch)>char_dic[ch]:
                    check = False
                    break
                else:
                    count +=1
            if check:
                tot+=count

        return tot
