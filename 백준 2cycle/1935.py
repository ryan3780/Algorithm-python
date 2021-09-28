# 다른 사람의 풀이
import sys
from collections import deque

input = sys.stdin.readline
 
N = int(input())
postfix = input()
alpha = [0]*N

for i in range(N):
    alpha[i] = int(input())
stack = []

for t in postfix:
    if 'A' <= t <= 'Z':
        stack.append(alpha[ord(t)-ord('A')])
    else:
        b = stack.pop()
        a = stack.pop()
        if t == '+':
            stack.append(a+b)
        elif t == '-':
            stack.append(a-b)
        elif t == '/':
            stack.append(a/b)
        elif t == '*':
            stack.append(a*b)
print(f"{stack[0]:.2f}")