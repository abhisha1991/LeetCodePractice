# https://codefights.com/interview-practice/task/uX5iLwhc6L5ckSyNC
def firstNotRepeatingCharacter(s):
    if s is "":
        return '_'

    if len(s) == 1:
        return s

    s = list(s)
    for i in range(0, len(s)):
        temp = s[i]
        s[i] = '#'
        if temp not in s:
            return temp
        else:
            s[i] = temp

    return '_'


# firstNotRepeatingCharacter("abacabad")
# firstNotRepeatingCharacter("abacabaabacaba")
# firstNotRepeatingCharacter("bcb")
firstNotRepeatingCharacter("ngrhhqbhnsipkcoqjyviikvxbxyphsnjpdxkhtadltsuxbfbrkof")