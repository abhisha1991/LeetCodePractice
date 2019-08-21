#https://leetcode.com/problems/unique-morse-code-words/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_lst = []
        morse_dic = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        for word in words:
            morse_word = ''
            for letter in word:
                morse_word+=morse_dic[ord(letter)-97]
            morse_lst.append(morse_word)
        un = len(set(morse_lst))
        return un
