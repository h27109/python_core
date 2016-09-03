
def getlines(n):
    name = raw_input("input file name:")
    f = open(name, 'r')
    x = 0
    for line in f:
        if x < n:
            print line,
            x += 1
        else:
            break
    f.close()

def getlinecount():
    name = raw_input("input file name:")
    f = open(name, 'r')
    count = len(f.readlines())
    f.close()
    return  count

def showfilein25lines():
    name = raw_input("input file name:")
    f = open(name, 'r')
    for x,line in enumerate(f):
        print x,":",line,
        if (x+1) % 25 == 0:
            if raw_input('press any key to continue'):
                continue


if __name__ == '__main__':
    #getlines(2)
    #print getlinecount()
    showfilein25lines()