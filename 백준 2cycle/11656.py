import sys
input = sys.stdin.readline
 
words = input().rstrip()
suffix = []

for i in range(len(words)):
    suffix.append(words[i:])

for i in sorted(suffix):
    print(i)
