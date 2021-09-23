import sys
input = sys.stdin.readline

q_num = int(input())

stack = []

def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0 :
        print(-1)
    else:
        print(stack.pop())


def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])


for i in range(q_num):
    command = input().strip()
    if len(command.split(' ')) > 1:
        push_num = command.split(' ')[1].replace('\n','')
        push(push_num)
    if command == 'pop':
        pop()
    if command == 'top':
        top()
    if command == 'size':
        size()
    if command == 'empty':
        empty()