import sys
input = sys.stdin.readline

shorts = []

for i in range(9):
    shorts.append(int(input()))

shorts = sorted(shorts)
total = 0

ans = []
for i in range(len(shorts)):
    for j in range(7):
        if total != 100:
            total += shorts[j]
        ans.append(shorts[j])

print(ans)