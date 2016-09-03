name1=raw_input("input file1")
name2=raw_input("input file2")

f1=open(name1,'r')
f2=open(name2,'r')

f3=open('newfile.txt','w')

for line in f1:
    f3.write(line)
for line in f2:
    f3.write(line)

f1.close()
f2.close()
f3.close()