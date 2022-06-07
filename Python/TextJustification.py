# https://leetcode.com/problems/text-justification
class Solution:
    def fullJustify(self, words, maxWidth):
        n = len(words)
        # i is current word's index
        i = 0
        res = []
        
        def getKWordsFromi(i):
            # k is going to be an index
            # such that words[i: i+k] are going to be the max number of words that can fit in that line
            k = 0
            # must join with spaces between words, there should be at least 1 space
            line = ' '.join(words[i : i+k])
            
            # while we can add words by incrementing k, such that our line formed (concating words) with spaces
            # is less than maxWidth and such that i + k <= total number of words
            while len(line) <= maxWidth and i + k <= n:
                k +=1
                line = ' '.join(words[i : i+k])
            
            # at this point, k is 1 word too much
            k -=1
            return k
        
        def getLineWithAdditionalSpacesBetweenWords(i, k):
            # so far we have words[i : i + k], and line = ' '.join(words[i : i+k])
            # ie, line is consisting of single spaced separated words between ith and kth index
            line = ' '.join(words[i : i+k])
            # 'final' below is going to be our line with additional spaces 
            
            # k would be 1 when we could only add a single word to line, ie, if the word was too large and almost = maxwidth
            # i + k would be equal to n if we're adding our last line
            # in both such cases, we need to "left justify" instead of trying to add additional spaces between words
            if k == 1 or i + k == n:
                spaces = maxWidth - len(line)
                final = line + (' ' * spaces)
                
            else:
                # this is counting total number of spaces that need to be distributed between the words
                # say if maxWidth was 10, and line so far was "cat dog"
                # then k = 2, ie, 2 words are there and len(line) = 7, ie, 6 char + 1 space
                # so spaces below is going to be 10 - 7 + 1 = 4
                # why? abs(-7+1) = 6, which is just the number of char in line, without spaces
                # so what we're saying below is, let's strip the line so far off all spaces, and lets calculate
                # total number of spaces that we need to distribute in between words, so we need to distribute 4 spaces
                # in total for this line
                spaces = maxWidth - len(line) + (k-1)
                
                guaranteedSpacesBetweenWords = int(spaces / (k-1))
                remainderSpaces = spaces % (k-1)
                
                # if we don't have remainder spaces and they divide evenly, then evenly distribute spaces between words
                if remainderSpaces == 0:
                    final = (' ' * guaranteedSpacesBetweenWords).join(words[i: i + k])
                else:
                    # we will partition i through i+k into 2 parts, i:i+left, i+left:i+k
                    # this will help meet the criteria in question:
                    '''
                    If the number of spaces on a line does not divide evenly between words, 
                    the empty slots on the left will be assigned more spaces than the slots on the right.
                    '''
                    left = remainderSpaces
                    # give more spaces to left words, ie, between words i and i+left, give more spaces
                    final = (' ' * (guaranteedSpacesBetweenWords+1)).join(words[i : i + left])
                    final += (' ' * (guaranteedSpacesBetweenWords+1))
                    # for the far right words, ie, between i + left and i + k, give only minimal space, ie, guaranteed space
                    final += (' ' * guaranteedSpacesBetweenWords).join(words[i + left: i + k])
                
            return final
        
        # main algo
        while i < n:
            k = getKWordsFromi(i)
            line = getLineWithAdditionalSpacesBetweenWords(i, k)
            res.append(line)
            # we have to increment i by k, since we have added a line in result that covers i to i + k
            i +=k
        return res