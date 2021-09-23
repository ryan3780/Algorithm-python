import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    ps = input().rstrip()
    stack = []
    for j in ps:
        if j == '(':
            stack.append(0)
        else:
            if len(stack) > 0 :
                stack.pop()
            else:
                stack.append(1)
                break
    print(stack)
    if stack:
        print('NO')
    else:
        print('YES')
# for i in range(n):
#     ps = input().rstrip()
#     cnt = 0
#     for j in ps:
#         if cnt < 0:
#             cnt -= 1
#             break
#         if j == '(':
#             cnt += 1
#         else:
#             if ps[0] == ')':
#                 cnt -= 1
#                 break
#             cnt -= 1
        
#     if cnt == 0:
#         print('YES')
#     else:
#         print('NO')