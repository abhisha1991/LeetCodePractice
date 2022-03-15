# https://stackoverflow.com/questions/63132258/minimum-total-area-of-at-most-two-banners-to-cover-n-buildings
'''
There are N rectangular buildings standing along the road next to each other. The width of every building is 1
The Kth building is of size Hk x 1. 

Because a renovation of all of the buildings is planned, 
we want to cover them with rectangular banners until the renovations are finished. 
Of course, to cover a building, the banner has to be at least as high as the building. 
We can cover more than one building with a banner.

We can order at most two banners and we want to cover all of the buildings. 
Also, we want to minimize the amount of material needed to produce the banners.
What is the minimum total area of at most two banners which cover all of the buildings?

For example, to cover buildings of heights [3, 1, 4] we could use a banner of area 10
    =
=   =
=   =
= = =

We will cover this such that buildings [3,1] are covered with 1 banner of height 3 and width 2 => 3x2 = 6
and the other building [4] will be covered with a height of 4 and width 1 => 4x1 = 4, this gives 6+4=10

This is the least area needed by the banners. If we used 1 banner (since we can use at most 2) -- we would get an area of 4x3 = 12, which is more than 10
'''
import sys
def minBannerArea(buildings):
    n = len(buildings)
    if n == 0:
        return 0
    
    if min(buildings) < 0:
        return 0

    if n == 1:
        return buildings[0] * 1
    
    # left contains a left to right pass over the buildings
    # right contains a right to left pass over the buildings
    # 0th element of left will assume, we cover 0th building only with 1 banner
    # 1st element of left will assume, we cover 0th and 1st buildings with 1 banner
    # 2nd element of left will assume, we cover 0th, 1st, 2nd buildings with 1 banner and so on
    # similarly, the right arr will contain last element such that we cover the last building only with 1 banner
    # 2nd last element of right arr will contain nth and n-1th buildings covered with 1 banner and so on
    # notice that if there are 2 banners, one of the building coverings MUST start from left and the other MUST start from the right in order to cover all buildings
    left = []
    right = []
    maxh = -sys.maxsize
    for i in range(n):
        if maxh < buildings[i]:
            maxh = buildings[i]

        left.append(maxh * (i+1))
    
    maxh = -sys.maxsize
    for i in range(n-1, -1, -1):
        if maxh < buildings[i]:
            maxh = buildings[i]

        right.append(maxh * (n-i))
    
    # we need to reverse right because we added to it in reverse order
    right.reverse()
    # banner will contain the area
    banner = []
    for i in range(n):
        if i == n-1:
            banner.append(left[i])
            continue

        area = left[i] + right[i+1]
        banner.append(area)

    # return min area
    print(f"For buildings {buildings}, the min area is {min(banner)}") 
    return min(banner)

minBannerArea([3,1,4])
minBannerArea([3,1])
minBannerArea([3])
minBannerArea([5, 3, 2, 4])
minBannerArea([5, 3, 5, 2, 1])
minBannerArea([7, 7, 3, 7, 7]) 
minBannerArea([3,4,5,6,7,8,9])
