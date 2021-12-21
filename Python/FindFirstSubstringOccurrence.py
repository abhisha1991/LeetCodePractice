def findFirstSubstringOccurrence(s, x):
    if x == "":
        return -1
    try:
        return s.index(x)
    except:
        return -1


print(findFirstSubstringOccurrence("abc", "d"))
print(findFirstSubstringOccurrence("abc", "a"))
print(findFirstSubstringOccurrence("aBcDefghaBcdEFgh", "ghb"))
print(findFirstSubstringOccurrence("abc", ""))
