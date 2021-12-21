# https://codefights.com/interview-practice/task/pMvymcahZ8dY4g75q
def firstDuplicate2(a):
    if a is []:
        return -1
    a_dict = dict()
    for i in range(0, len(a)):
        element = a[i]
        if element not in a_dict.keys():
            a_dict[element] = [i]
        else:
            temp = list(a_dict[element])
            temp.append(i)
            a_dict[element] = temp

    list_second_occur = list()
    for key in a_dict.keys():
        if len(a_dict[key]) > 1:
            temp = list(a_dict[key])
            list_second_occur.append(temp[1])

    if len(list_second_occur) is 0:
        return -1

    smallest_index = min(list_second_occur)
    return a[smallest_index]


def firstDuplicate(A):
    for i, x in enumerate(A):
        A[abs(x) - 1] *= -1
        if A[abs(x) - 1] > 0:
            return abs(x)
    return -1

firstDuplicate([2, 3, 3, 1, 5, 2])
firstDuplicate([2, 4, 3, 5, 1])