# https://codefights.com/interview/DGnaZ3J5hnWS6xYJy
def reverseSentence(sentence):
    split_input = sentence.split()
    result = ""
    split_input.reverse()
    for w in split_input:
        result = result + w + " "
    return result[0: len(result) - 1]  # remove extra space


print(reverseSentence("BgwlaMUMkToumKe ANHz"))
print(reverseSentence("Man bites dog"))
print(reverseSentence("IHateSpaces"))
print(reverseSentence("a b c"))
