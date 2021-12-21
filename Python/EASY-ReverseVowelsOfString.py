# https://codefights.com/interview/9JbYrEhK9tz6ANKLC
def reverseVowelsOfString(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s_vowels = []
    s_list = list(s)
    i = 0
    special_char = '+'
    for ch in s_list:
        if ch in vowels:
            s_vowels.append(ch)
            s_list[i] = special_char
        i = i + 1
    j = 0
    k = len(s_vowels) - 1
    for ch in s_list:
        if ch is special_char:
            s_list[j] = s_vowels[k]
            k = k - 1
        j = j + 1

    return "".join(s_list)


print(reverseVowelsOfString("Sore was I ere I saw Eros."))
