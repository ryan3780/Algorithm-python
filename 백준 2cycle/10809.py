import sys

input = sys.stdin.readline

n = input().rstrip()

alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
result = [n.index(i) if i in n else -1 for i in alphabet ]

print(*result)