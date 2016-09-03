g = lambda x: x%2==0
f = lambda x: x*5
j = lambda x,y: x+y
print filter(g, range(1,10))
print '*'*10

def myfilter(func, nargv):
    ret = []
    for item in nargv:
        if func(item):
            ret.append(item)
    return  ret

print myfilter(g, range(1,10))
print '*'*10

from random import randint as ri
print [n for n in [ri(1,99) for i in range(9)] if n%2]
print '*'*10

print map(f, range(1,10))
print '*'*10

print map(j, range(1,10), range(5,14))
print '*'*10

print [n*5 for n in range(1,10)]
print '*'*10

print reduce(j, range(1,101))
print '*'*10
