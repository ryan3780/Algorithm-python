import sys

input = sys.stdin.readline

N = input().rstrip()

p = 'AAAA'
m = 'BB'

a = N.replace('XXXX', p)
b = a.replace('XX', m)

if 'X' in b:
    print(-1)
else:
    print(b)
