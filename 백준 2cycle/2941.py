import sys

input = sys.stdin.readline

c_alpha = input().rstrip()

trans_list = ['c=', 'c-',  'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in trans_list:
    c_alpha = c_alpha.replace(i, '?')
    
print(len(c_alpha))    