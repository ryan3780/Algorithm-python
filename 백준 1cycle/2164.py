import sys
from collections import deque

input = sys.stdin.readline

card = deque()

n = int(input())

for i in range(1, n+1):             # N
    card.append(i)

while n > 0:                        # N
    if len(card) == 1:
        break
    card.popleft()
    card.append(card.popleft())
    n -= 1

print(card.pop())                   # O(N + N) == O (N)