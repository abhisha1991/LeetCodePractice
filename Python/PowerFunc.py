# refer to section 4.7 for power function explanation in EPI book
def powerfunc(x, power):
    if power < 0:
        power = -power # make power positive
        x = 1/x
    return helper(x, power)

def helper(x, power):
    if power == 0:
        return 1
    if power % 2 == 0:
        res = helper(x * x, power >> 1)
    else:
        res = x * helper(x * x, power >> 1)
    return res


print(powerfunc(2, 3))
print(powerfunc(2, 4))
print(powerfunc(-2, 4))
print((powerfunc(-2, -4)))
print(powerfunc(2,0))
print(powerfunc(2, 56))