# https://leetcode.com/problems/string-transforms-into-another-string/
class Solution: 
    def canConvert(self, str1: str, str2: str) -> bool:
        # if 2 strings are not of same length, that's an easy reject
        # you can't convert abc to ab or vice versa
        if len(str1) != len(str2):
            return False
        
        # obvious one
        if str1 == str2:
            return True
        
        # graph contains state transition mapping for each char in str1 to str2
        # aabcc --> ddbee, here every char in source maps only to a single char in dest
        # a maps to d, b maps to b, c maps to e -- so we can convert this

        # if we had a situation like 
        # aabc --> dfxy, while b and c map to a single char each (x and y), a maps to 2 chars (d and f)
        # in this case, we can't convert 
        graph = dict()
        dests =  set()
        
        for i in range(len(str1)):
            source = str1[i]
            dest = str2[i]
            
            if source not in graph:
                graph[source] = dest
                dests.add(dest)
                
            else:
                # we are capturing the 1:n cardinality entry here for aabc --> dfxy case here for "a"
                if dest != graph[source]:
                    return False
        
        # consider other cases that seem non-solvable but are actually solvable
        # consider abc --> cab, at first glance we have mapping {a: c, b: a, c: b} - single char in source, maps to single char in dest
        # so far so good...
        # if we convert any of the chars first, say "a" converts to "c" and "b" converts to "a"
        # cac --> this implies that we can't convert this to "cab" since the conversion of "c" in source next now will replace 
        # the 1st and 3rd char - becoming bbb
        # instead have the following map {a: z, b: a, c: b, z: c}, giving abc --> zbc --> zac --> zab --> cab (redirection strategy)
        
        # this can be done if there were multiple cycles too! for example, abcdef --> cabfde 
        # can also be converted (using 2 diff redirection char, say z and y)
        # {a: z, b: a, c: b, z: c, d: y, e: d, f: e, y: f}, giving
        # abcdef --> zbcdef --> zacdef --> zabdef --> cabdef --> cabyef --> cabydf --> cabyde --> cabfde
        # in fact, we don't even need 2 distinct redirection char (z and y), we can reuse chars (only 1 is sufficient)
        # dont declare a full dictionary mapping for all chars, do this in parts
        # {a: z, b: a, c: b, z: c} --> abcdef --> zbcdef --> zacdef --> zabdef --> cabdef
        # {d: z, e: d, f: e, z: f} --> cabdef --> cabzef --> cabzdf --> cabzde --> cabfde
        
        # we can only have lower case chars in our redirection strategy (since input can have only lowercase chars), so if all 26 chars are already present
        # there's no way left to redirect to something that is unused (z in above example)
        # so if "dests" contained 26 unique letters, this would be false!
        if len(dests) < 26:
            return True
        
        # actually attempt to convert str1 to str2
        # keys will be a set of chars that have been converted so far
        keys = set()
        lk = len(keys)
        while str1 != str2 and keys != set(graph.keys()):
            # this may seem like o(n2) but its not since graph can only contain 26 elements worst case (lower case letters)
            for k,v in graph.items():
                if k in keys or v in str1:
                    continue
                keys.add(k)
                # replace all instances of earlier source char to new dest char
                str1 = str1.replace(k,v)
                
            # if we're not making further progress by adding to our processed 'keys' set in every iteration
            # then we cant convert a given string to another
            if lk == len(keys):
                return False
            else:
                lk = len(keys)
        
        return True