import sys
from itertools import combinations

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

_sum = K*(K+1) // 2

if _sum > N:
    print(-1)
elif (N - _sum) % K == 0:
    print(K-1)
else:
    print(K)

# 결과는 맞을거 같은데, 시간초과인 풀이 방법

# ball = [ x for x in range(1, N+1)]
# ans = []
# # print(ball, basket)

# for i in combinations(ball, K):
#     if sum(i) == N:
#         ans.append(i)

# print(ans)
# if len(ans) == 0:
#     print(-1)
# else:
#     print(abs(ans[-1][0] - ans[-1][K-1]))



