import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

class Que:
    def __init__(self):
        self.que = []
    def push(self, num):
        self.que.append(num)
    def pop(self):
        return self.que.pop(0) if len(self.que) != 0 else -1
    def size(self):
        return len(self.que)
 
    def empty(self):
        return 1 if self.size() == 0 else 0
 
    def front(self):
        return self.que[0] if self.size() != 0 else -1
 
    def back(self):
        return self.que[-1] if self.size() != 0 else -1

que = Que()

for i in range(n):
    command = input().split()
    if command[0] == "push":
        que.push(command[1])
    elif command[0] == "pop":
        print(que.pop())
    elif command[0] == "size":
        print(que.size())
    elif command[0] == "empty":
        print(que.empty())
    elif command[0] == "front":
        print(que.front())
    elif command[0] == "back":
        print(que.back())
    
    