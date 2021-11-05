import sys
input = sys.stdin.readline

e, s, m = map(int, input().split())
i, j, k = 1, 1, 1

ans = 0

while True:
    ans += 1

    if e == i and s == j and m == k:
        print(ans)
        break

    i += 1
    j += 1
    k += 1

    if i == 16:
        i = 1
    if j == 29:
        j = 1
    if k == 20:
        k = 1
