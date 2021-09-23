import sys

input = sys.stdin.readline

f_num, s_num = input().split()

f_num, s_num = f_num[::-1], s_num[::-1]

if int(f_num) > int(s_num):
    print(f_num)
else:
    print(s_num)