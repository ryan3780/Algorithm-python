import sys
input = sys.stdin.readline

s = set()

def add(x):
    s.add(x)


def remove(x):
    try:
        s.remove(x)
    except:
        pass


def check(x):
    if x in s:
        return 1
    return 0


def toggle(x):
    if x in s:
        s.remove(x)
    else:
        s.add(x)


def all():
    global s
    s = set([i for i in range(1,21)])
   

def empty():
    global s
    s.clear()
  

n = int(input())

for i in range(n):
   
    word  = input().split()
       

    if word[0] == 'add':
        add(int(word[1]))
    elif word[0] == 'check':
        print(check(int(word[1])))
    elif word[0] == 'remove':
        remove(int(word[1]))
    elif word[0] == 'toggle':
        toggle(int(word[1]))
    elif word[0] == 'all':
        all()
    elif word[0] == 'empty':
        empty()