# https://leetcode.com/problems/synonymous-sentences/
from collections import defaultdict
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        dic = defaultdict(set)
        
        # add synonyms both ways
        # happy --> joy
        # joy --> happy
        for s in synonyms:
            dic[s[0]].add(s[1])
            dic[s[1]].add(s[0])
        
        res = set()
        # initialize the q with text
        q = [text]
        
        # bfs
        while len(q) > 0:
            t = q.pop()
            
            # add text to res as soon as you pop
            res.add(t)
            
            # we know that the words are split on spaces
            words = t.split(' ')
            
            for i in range(len(words)):
                w = words[i]
                
                # notice how 'w' can be both "happy" and "joy"
                # initial text object 't' will have -- "I am happy and strong"
                # then we will replace 'happy' with a synonym word in pos 'i', ie, 'joy' goes in pos 'i'
                # this then gets added to the queue as "I am joy and strong", since its not in res yet
                # when we process synonyms of 'joy', we'll be able to get to words like 'cheerful' etc. 
                # (this is how we access tertiary synonyms)
                
                # notice after we have processed "I am happy and strong" and replaced with "I am joy and strong"
                # we will next come after replacement of "strong" with its synonyms -- due to bfs
                if w in dic:

                    # if 'w' happens to be one of the special words, then look into its synonyms
                    for syn in dic[w]:
                        # create a new list of words to create new text
                        # replace the ith place with special synonym word of 'w'
                        # notice how we're passing [syn] as a list to concat as list
                        new_words = words[:i] + [syn] + words[i+1:]
                        
                        # create new text by joining on spaces
                        new_t = " ".join(new_words)
                        
                        # this safeguards us from going into infinite loop
                        if new_t not in res:
                            q.append(new_t)

        return sorted(list(res))