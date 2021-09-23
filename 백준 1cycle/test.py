import random

winning = [sorted(random.sample(range(1,46),6)) for x in range(5)]

for i, win in enumerate(winning):
    for j in range(len(winning)):
        if winning[i][j] < 10:
            winning[i][j] = '0' + str(winning[i][j])

    if i == 0:
        print()
        print(str(win).strip('[]').replace(',','').replace('[', '').replace(']', '').replace("'",''))
    elif i == 4:
        print(str(win).strip('[]').replace(',','').replace('[', '').replace(']', '').replace("'",''))
        print()
    else:
        print(str(win).strip('[]').replace(',','').replace('[', '').replace(']', '').replace("'",''))