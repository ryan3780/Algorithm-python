import sys

input = sys.stdin.readline

N = int(input())
C = [int(input()) for i in range(N)]

sorted_c = sorted(C,reverse=True)
_list = []

for i in range(0, N, 3):
    num = sorted_c[i:i+3]
    _list.append(num)

_sum = 0

for milk in _list:
    if len(milk) == 3:
        _sum += sum(milk) - milk[-1]
    else:
        _sum += sum(milk)

print(_sum)