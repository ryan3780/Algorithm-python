import sys

input = sys.stdin.readline

a = input()
b = input()

ans = []

for i in range(3):
    ans.append(int(a)*int(b[i]))
    
for i in range(1,4):
    print(ans[-i])

for i in range(1,4):
    ans[-i] = ans[-i] * 10 ** i / 10
    ans[-i] = int(ans[-i])

print(sum(ans))