import sys

input = sys.stdin.readline

h, m = map(int, input().split())

if m <= 45:
    h = h -1
    m = m + 15
    if m == 60:
        m = 0
        h = h + 1
    if h < 0:
        h = 23    
    print(h, m)
else:
    m = m - 45
    print(h, m)