from abc import abstractproperty
import sys

input = sys.stdin.readline

n = int(input())
people = []
for i in range(n):
    each = list(map(int, input().split()))
    people.append(each)


result = []
for i in range(n):
    k = 1
    for j in range(n):
        # print(people[i][0], people[j][0], people[i][1], people[j][1])
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            print(people[i])
            people[i].append(k)
            k +=1
    result.append(k)

print(*result)