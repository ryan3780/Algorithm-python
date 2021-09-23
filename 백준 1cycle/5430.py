import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())

# 명령어 리스트로
for i in range(N):
    _cmd = list(map(str, input().replace('RR','').strip()))
    _len_list = int(input().strip())
    _list = deque(input().replace('[','').replace(']','').replace(' ', '').strip().split(','))

    reverse = False
    
    if '' in _list:
        print('error')
        break
    else:

        for cmd in _cmd:
            if cmd == 'R':
                reverse = True
            else:
                if len(_list) == 0:
                    print('error')
                    break
                else:
                    if reverse == True:
                        _list.pop()
                    else:
                        _list.popleft()

    if reverse == True:
        result = list(map(int, _list))
        result = sorted(result, reverse=reverse)
        print(f'[{",".join(list(map(str, result)))}]')
    else:
        result = list(map(int, _list))
        print(f'[{",".join(list(map(str, result)))}]')
