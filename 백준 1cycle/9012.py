import sys
input = sys.stdin.readline

q_num = int(input())

for i in range(q_num):
    bracket = input().strip()
    # stack = []

    # if len(bracket) < 2:
    #     print('NO')
    
    # cnt = 0

    # for item in bracket:
    #     if item == '(':
    #         stack.append(item)
    #         cnt += 1
    #     else:
    #         if len(stack) > 0:
    #             stack.pop()
    #             cnt -= 1
    #         else:
    #             cnt += 1  

    # if len(stack) == 0 and cnt == 0:
    #     print('YES')
    # else:
    #     print('NO')    

    left = 0
    cnt = 0

    for item in bracket:
        if item == '(':
            left +=1
        else:
            if left == 0:
                cnt += 1
            else:
                left -= 1
        
    if left == 0 and cnt == 0:
        print('YES')
    else:
        print('NO')