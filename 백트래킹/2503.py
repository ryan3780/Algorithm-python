import sys

input = sys.stdin.readline

n = int(input())
q = []

for i in range(n):
    question, strike, ball = input().split()
    q.append([question, strike, ball])

tmp = 0

ball = 0


while True:
    arr = []
    for i in range(100, 1000):
        base = str(i)
        
        for j in range(n):
            strike = 0
            for k in range(n-1):
                
                if base[k] == q[j][0][k]:
                    strike += 1
                    print(base, strike, q[j][1])
                    if strike == q[j][1]:
                        print('???')
                # elif base[k] in q[j][0][k]:
                #     ball += 1
    
    break
