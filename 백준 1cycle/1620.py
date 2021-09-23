import sys
input = sys.stdin.readline

p_num, q_num = map(int, input().split())

arr = []
q_dic = {}

for i in range(p_num):
    poket = input().strip()
    arr.append(poket)
    q_dic[poket] = i + 1

for i in range(q_num):
    question = input().strip()
    if question.isdigit():
        print(arr[int(question) - 1])
    else:
        print(q_dic[question])
