# 다른 사람의 풀이
import sys
import re
input = sys.stdin.readline
 
iron_stick = input().rstrip()
cnt = 0
stack = []

for i in range(len(iron_stick)):
    if iron_stick[i] == '(':
        stack.append('(')
    else:
        if iron_stick[i-1] == '(' :
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
print(cnt)