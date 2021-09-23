import sys

input = sys.stdin.readline

word = input().rstrip()

set_word = set(word)

print(set_word)

_dict = {}

for i in range(len(word)):

    _dict[word[i]] = word.count(word[i])

ans = [k for k, v in _dict.items() if max(_dict.values()) == v]


if len(ans) > 1:
    print('?')
else:
    print(ans[0].upper())

# import sys

# input = sys.stdin.readline

# word = input().rstrip().upper()

# set_word = list(set(word))

# ans = []
# for i in set_word:
#     cnt = word.count(i)
#     ans.append(cnt)

# # print(len(set_word), len(ans))

# if ans.count(max(ans)) > 1:
#     print('?')
# else:
#     print(set_word[ans.index(max(ans))])


