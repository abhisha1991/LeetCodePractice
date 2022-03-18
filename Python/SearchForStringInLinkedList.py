# asked in outreach.io
# You are given a very very long string in the form of a linkedlist
# presumably, this string can't fit in one contiguous memory block of "string" data type 
# so you need to chunk it out in the form of linked list nodes connected to each other
# task is to find a target string in this very long string data structure

'''
Needle in a Haystack problem 

haystack1 = "abcd" --> "efgh" --> "ijk"
haystack2 = "abcd" --> "ef" --> "gh" --> "i" --> jk"
haystack3 = "a"--> "b" --> "c" --> "d" --> "e" --> "f" --> "g" --> "h" --> "i" --> "j" --> "k"

stored as a linked list
haystack1 is basically the same as haystack2 is the same as haystack3

contains(haystack1, needle="abc") --> true
contains(haystack1, needle="def") --> true
contains(haystack1, needle="ghi") --> true
contains(haystack1, needle="cba") --> false
contains(haystack1, needle="") --> true

You are NOT allowed to concat the string parts of the linked list, simply because you cant store that long a string in memory
'''
class Node:
    def __init__(self, text):
        self.text = text
        self.next = None

def contains(haystack, needle):
    if len(needle) == 0 or needle is None:
        return True
    
    if haystack is None:
        return False

    # contains a map of the position number of the node to the node reference
    # this means that we are going to be referencing the data and are not copying new objects into the dictionary
    # so the memory use is only going to be trivial here
    nodeMap = dict()
    
    # contains tuples of 2 such that first is identifying which node we're in, second is identifying what is the position number of the char in the text of the node 
    iterator = []

    nodeNum = 0
    # create and iterator by going through the haystack and each char of each node of the haystack
    # time complexity is len(haystack) * len(data) because it takes that much time to create the iterator
    while haystack != None:
        nodeMap[nodeNum] = haystack
        data = haystack.text

        for j in range(len(data)):
            iterator.append((nodeNum, j))

        haystack = haystack.next
        nodeNum +=1

    n = 0
    for i in iterator:
        node = nodeMap[i[0]]
        idx = i[1]
        
        # if there's no match, reset n to zero and continue
        if n < len(needle) and needle[n] != node.text[idx]:
            n = 0
            continue

        # keep incrementing the counter if there's a match
        if n < len(needle) and needle[n] == node.text[idx]:
            n +=1
        
        if n == len(needle):
            return True
    
    return False


# generate the linked list
hs = Node("abcd")
hs.next = Node("efgh")
hs.next.next = Node("ijk")
hs.next.next.next = Node("abcdee") # repeat pattern

print(contains(hs, needle="abc"))
print(contains(hs, needle="def"))
print(contains(hs, needle="ghi"))
print(contains(hs, needle="j"))
print(contains(hs, needle=""))
print(contains(hs, needle="ca"))
print(contains(Node(""), needle=""))
print(contains(Node(""), needle="x"))
print(contains(hs, needle="abcdf"))
print(contains(hs, needle="abcdef"))
print(contains(hs, needle="abcdee"))