# asked in abacus.ai
# replace consecutive characters of a string with a '+'
# example --> aabbc becomes ++++c, abbabc becomes a++abc
def convert(s):
    arr = [''] * len(s)
    if len(s) <= 1:
        arr = [s]
        print(f"for string {s}, the result is {arr}")
        return arr

    i = 0
    while i < len(s):
        cur = s[i]
        j = i+1
        breaking = False

        # this is still o(n) because we have to iterate through every char only once
        # look at the line just above breaking=True below
        while j < len(s):
            # print(f"i is {i} and j is {j}")
            if cur == s[j]:
                arr[i] = '+'
                arr[j] = '+'
            else:
                if arr[i] == '':
                    arr[i] = cur
                    arr[j] = s[j]
                i = j
                breaking = True
                break
            j +=1
                
        if not breaking:
            i +=1

    # if the last char is still not set, set it
    if arr[-1] == '':
        arr[-1] = s[-1]

    print(f"for string {s}, the result is {arr}")
    return arr


convert('')
convert('a')
convert('ab')
convert('abbcbc')
convert('abbccb')
convert('abbccbc')
convert('aaaa')
convert('aaaabbbb')
convert('abababab')
convert('aabbccde')
convert('abcaabb')