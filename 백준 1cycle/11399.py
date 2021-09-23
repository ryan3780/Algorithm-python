import sys

input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
_P = P[:]

times = sorted(P)
_sum = 0

for i in range(N + 1):
    _sum += sum(times[:i])

print(_sum)

# ans = []

# for i in range(N):
#     _min = P.index(min(P))
#     ans.insert(i, _min + 1)
#     P[_min] = 1001

# cnt = []

# for i in range(N):
#     cnt.append(_P[ans[i] - 1])

# result = []
# for i in range(N+1):
#     result.append(cnt[:i])

# del result[0]

# fin = []

# for i in result:
#     fin.append(sum(i))
    
# print(sum(fin))



