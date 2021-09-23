import sys

input = sys.stdin.readline

n, m = map(int, input().split())

cards = list(map(int, input().split()))

sorted_cards = sorted(cards)
result = 0


for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            # print(sorted_cards[i] , sorted_cards[j] ,sorted_cards[k])
            if sorted_cards[i] + sorted_cards[j] + sorted_cards[k] > m :
                continue
            else:
                result = max(result, sorted_cards[i] + sorted_cards[j] + sorted_cards[k])
print(result)