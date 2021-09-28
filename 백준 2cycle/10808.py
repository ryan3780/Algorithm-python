import sys
input = sys.stdin.readline
 
words = input().rstrip()
alphabet = {}
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

for i in ascii_lowercase:
    alphabet[i] = words.count(i)

print(*list(alphabet.values()))