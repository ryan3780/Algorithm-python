import sys

input = sys.stdin.readline

N = input().rstrip()
money = int(N)
mod = money % 5
cnt = 0

if money == 1 or money == 3:
    print(-1)
elif mod % 2 == 0:
    print(money // 5 + mod // 2)
else:
    print(((money // 5) - 1) + (mod + 5) //  2)
