#!/usr/bin/env python3
def trail_0(n):
    c = 0
    i = 5
    while n/i>=1:
        c+=int(n/i)
        i*=5
    return int(c)

for _ in range(int(input())):
    n = int(input())
    print(trail_0(n))
