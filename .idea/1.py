f = open("a.txt", 'r')

#x=[word for line in f for word in line.split()]

#y = (word for line in f for word in line.split())

#for item in y:
#    print item

x=(len(line) for line in f)
maxlinelen=max(x)
print maxlinelen

print "x"*100

f.seek(0)
y=[line for line in f]
print y

