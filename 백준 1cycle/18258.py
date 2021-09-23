import sys
from collections import deque

input = sys.stdin.readline

readline = int(input())

my_que = deque()

def push(x):
    my_que.append(x)


def pop():
    if len(my_que) == 0:
        return -1
    else:
        return my_que.popleft()


def size():
    return len(my_que)


def empty():
    if size() == 0:
        return 1
    else:
        return 0
    
def front():
    if empty() == 1:
        return -1
    else:
        return my_que[0]
    

def back():
    if empty() == 1:
        return -1
    else:
        return my_que[-1]


for i in range(readline):
    command = input().strip()
    if len(command.split(' ')) > 1:
        push_num = command.split(' ')[1].replace('\n','')
        push(push_num)
    elif command == 'pop':
        print(pop())
    elif command == 'size':
        print(size())
    elif command == 'empty':
        print(empty())
    elif command == 'front':
        print(front())
    elif command == 'back':
        print(back())
