import sys
input = sys.stdin.readline
 
a, b, c, d = input().split()

mix_ab = a + b
mix_cd = c + d
print(int(mix_ab) + int(mix_cd))