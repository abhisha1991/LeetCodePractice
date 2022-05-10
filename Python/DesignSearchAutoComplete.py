# https://leetcode.com/problems/design-search-autocomplete-system
from collections import defaultdict
# this solution is space efficient, but not time efficient
# time efficient solution can be done with Trie, but that eats a lot of memory on internal stack
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.history = defaultdict(int)
        self.search = ''
        
        # this is the filtered search list
        # this keeps getting updated as we add more characters to our search term
        self.slist = []  
        
        # we need to return only top 3 elements by frequency from slist
        self.maxRet = 3
        
        for i in range(len(sentences)):
            self.history[sentences[i]] = times[i]
        
    def input(self, c: str) -> List[str]:
        # if we're ending our present search
        if c == '#':
            # add search so far to our history, not including the # char
            # increment its frequency by 1
            # we don't have to worry about 'search' not being a key in history
            # since we're using defaultdict
            self.history[self.search] += 1
            
            # reset search and search match list
            self.search = ''
            self.slist = []
            # return empty list as per problem description
            return self.slist
        
        # this means we're starting a new search
        # either immediately after a '#' or this is the first time we're searching 
        if self.slist == []:
            self.search += c
            # add k,v in slist
            # key is the sentence, value is the freq of that sentence
            for k,v in self.history.items():
                if k.startswith(self.search):
                    self.slist.append((k,v))
            
            # sort in decreasing order of frequency and increasing order of ascii sentence
            self.slist = sorted(self.slist, key=lambda x: (-x[1], x[0]))
            
            # only pick the i[0], ie, the sentence part and store in slist
            # note that at this point, we don't care about the frequency since we have already
            # sorted by frequency, if we pick first K elements in list, we are getting top K freq elements
            
            # also observe that if we filter this slist of size n later on, based on future search terms 
            # (general case, not part of this if case)
            # we STILL maintain the frequency ordering of the terms that end up in slist
            # ie, first K elements are STILL top K frequent elements
            # THIS IS A KEY OBSERVATION
            self.slist = [i[0] for i in self.slist]
            return self.slist[:self.maxRet]
        
        # lens = len(self.search)

        # general search case
        # add to your search string, the present char
        self.search += c
        
        # keep filtering the slist based on search term and re-assign to slist, 
        # since the search term going forward will keep appending to what was the previous search term
        # can use this instead as well: self.slist = [x for x in self.slist if len(x) > lens and x[lens] == c]
        self.slist = [x for x in self.slist if x.startswith(self.search)]
        return self.slist[:self.maxRet]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)