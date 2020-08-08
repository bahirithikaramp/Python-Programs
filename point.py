"""
A dictionary is a collection which is unordered, changeable and indexed.
In Python dictionaries are written with curly brackets, and they have keys and values.
"""

"""
Question: Chef has N axis-parallel rectangles in a 2D Cartesian coordinate system.
These rectangles may intersect, but it is guaranteed that all their 4N vertices are pairwise distinct.

Unfortunately, Chef lost one vertex, and up until now, none of his fixes have worked
(although putting an image of a point on a milk carton might not have been the greatest idea after all…).
Therefore, he gave you the task of finding it! You are given the remaining 4N−1 points and you should find the missing one.

"""

#CODE
#!usr/bin/env pyhton3
for _ in range(int(input())):
    l1 =[]
    l2 =[]
    n = int(input())
    for i in range(4*n-1):
        a,b = map(int,input().split())
        l1.append(a)
        l2.append(b)

    d1 = dict()
    for i in l1:
        if i not in d1:
            d1[i]=0
        d1[i]+=1
    d2 = dict()
    for i in l2:
        if i not in d2:
            d2[i]=0
        d2[i]+=1
    #print(d1,d2)
    for i,j in d1.items():
        if j%2!=0:
            x = i
    for i,j in d2.items():
        if j%2!=0:
            y = i
    print(x,y)
