import sys
input = sys.stdin.readline
 
words = input().rstrip()
prefix = []

for i in range(len(words)):
    prefix.append(words[i:])

for i in sorted(prefix):
    print(i)
