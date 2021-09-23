import sys

input = sys.stdin.readline

n = input().rstrip()

if int(n) < 10:
    n = "0" + n

calnum = n[1] + str(int(n[0]) + int(n[1]))[-1]
count = 1

while calnum != n:
    calnum = calnum[1] + str(int(calnum[0]) + int(calnum[1]))[-1]
    count += 1

print(count)