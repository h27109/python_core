
def isprime(number):
    n = number/2
    while n > 1:
        if number%n == 0:
            return False
        else:
            n -= 1
    return True

def getfactors(number):
    n = 1
    ret = []
    while n <= number:
        if number%n == 0:
            ret.append(n)
        n += 1
    return ret

allret = []
def getprimefactors(number):
     factors = getfactors(number)
     print  factors
     for item in factors:
         ret = []
         if item == 1 or item == number:
            continue
         else:
             if isprime(item):
                 ret.append(item)
             else:
                 ret.extend(getprimefactors(item))
             othervalue = number/item
             if isprime(othervalue):
                 ret.append(othervalue)
             else:
                 print "1-->", othervalue
                 ret.extend(getprimefactors(othervalue))
             allret.append(ret)

getprimefactors(20)
print allret
