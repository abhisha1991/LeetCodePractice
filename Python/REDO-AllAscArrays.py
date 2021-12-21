# correct answer, however, it is inefficient
def all_arrays(a, b):
    a0 = a[0]
    b = [x for x in b if x > a0]
    if len(b) == 0:
        return []
    result = []
    for i in a:
        for j in b:
            if i < j:
                result.append([i, j])

    lenres = len(result)
    i = 0
    while i < lenres:
        j = 0
        while j < lenres:
            x = []
            y = []
            x.extend(result[i])
            y.extend(result[j])
            x.extend(y)
            if x == sorted(x):
                result.append(x)
                lenres += 1
            j += 1
        i += 1

    print(result)
    return result

all_arrays([1, 2, 5, 11, 35], [10, 20, 30, 40])
x = len(all_arrays([1, 2, 5, 11, 45, 65, 67, 78, 88], [10, 20, 30, 40, 50, 80, 90, 100, 120]))
print(x)

'''
For Example 
A = {10, 15, 25}
B = {1, 5, 20, 30}
10 20
10 30
15 20
15 30
25 30

10 20 25 30
15 20 25 30


The resulting arrays are:
  10 20
  10 20 25 30
  10 30
  15 20
  15 20 25 30
  15 30
  25 30
'''

'''

A = {1, 2 , 5, 11}
B = {10, 20, 30}
1 10
1 20
1 30
2 10
2 20
2 30
5 10
5 20
5 30
11 20
11 30
1 10 11 20
1 10 11 30
2 10 11 20
2 10 11 30
5 10 11 20
5 10 11 30

[1, 10], [1, 20], [1, 30], [2, 10], 
[2, 20], [2, 30], [5, 10], [5, 20], [5, 30], 
[11, 20], [11, 30], [1, 10, 11, 20], [1, 10, 11, 30], 
[2, 10, 11, 20], [2, 10, 11, 30], [5, 10, 11, 20], [5, 10, 11, 30]
'''

