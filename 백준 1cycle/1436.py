import sys

input = sys.stdin.readline

N = int(input())
last_movie = 666

while N:
    if "666" in str(last_movie):
        N -= 1
    last_movie += 1

print(last_movie - 1)


