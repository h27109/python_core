def foo():
    m = 3
    def bar():
        n = 4
        print m + n
    print m
    bar()

def foo1():
    m = [1]
    def bar():
        print 'in bar', m[0]
        m[0]=2
    bar()
    print 'in foo1', m[0]

foo1()

def foo2():
    m = 1
    def bar():
        print 'in bar', m
        m=2
    bar()
    print 'in foo1', m

foo2()
