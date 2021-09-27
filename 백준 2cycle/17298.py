# 다른 사람의 풀이
import sys
from collections import deque

input = sys.stdin.readline
 
n = int(input())
arr = list(map(int, input().split()))
stack = []
answer = [-1 for i in range(n)]

for i in range(len(arr)):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    
    stack.append(i)
print(*answer)

# n = int(input().rstrip())
# a = list(map(int,input().split()))
# stack = deque()
# oh_big = [-1] * n

# for i in range(n):
#     while stack and (stack[-1][0] < a[i]):
#         print(stack[-1][0])
#         tmp, idx = stack.pop()
#         oh_big[idx] = a[i]
#     stack.append([a[i], i])

# print(oh_big)
