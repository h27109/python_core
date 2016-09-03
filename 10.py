
def foo(thefirst, thesecond, *therest, **therestdic):
    print "the first:", thefirst
    print "the second:", thesecond
    print "the rest:", therest
    print "the rest dic:", therestdic
    print
def newfoo(arg1, arg2, *nkw, **kw):
    'display regular args and all variable args'
    print 'arg1 is:', arg1
    print 'arg2 is:', arg2
    for eachNKW in nkw:
        print 'additional non-keyword arg:', eachNKW
    for eachKW in kw.keys():
        print "additional keyword arg '%s': %s" % \
    (eachKW, kw[eachKW])

if __name__ == "__main__":
    foo('1st', '2nd')
    foo('1st', '2nd', '3rd', '4th')
    foo('1st', '2nd', '3rd', '4th', five='5th', six='6th')
    aTuple = ('1','2')
    aDic={'a':1,'b':2}
    foo('1st', second = '2nd', *aTuple, **aDic)

    aTuple = (6, 7, 8)
    aDict = {'z': 9}
    newfoo(1, 2, 3, x=4, y=5, *aTuple, **aDict)