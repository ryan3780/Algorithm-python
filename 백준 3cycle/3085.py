import sys
input = sys.stdin.readline

n = int(input())
candy_color = []

for i in range(n):
    candy_color.append(input().rstrip())

print(candy_color)