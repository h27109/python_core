db = {}

import time
import md5
import os
import pickle
import shelve

def encrypt(str):
    if type(str) != type('a'):
        return -1
    ob=md5.md5()
    ob.update(str)
    return ob.hexdigest()

def newuser():
    prompt = 'login desired: '
    while True:
        name = raw_input(prompt).lower()
        for chr in name:
            if not (chr.isdigit() or chr.isalpha()):
                print "name is invalid"
                return
        if db.has_key(name):
            prompt = 'name taken, try another: '
            continue
        else:
            break
    pwd = raw_input('passwd: ')
    value=[]
    value.append(encrypt(pwd))
    value.append(0)
    db[name] = value
    savetofile3()

def olduser():
    name = raw_input('login: ').lower()
    for chr in name:
        if not (chr.isdigit() or chr.isalpha()):
            print "name is invalid"
            return
    pwd = encrypt(raw_input('passwd: '))
    value = db.get(name)
    if value == None:
        print "The name is not exist"
        choice = raw_input("do you want add this user?")
        if choice == 'y':
            value = []
            value.append(pwd)
            value.append(0)
            db[name] = value
            return
    passwd = value[0]
    lsttime = value[1]
    if passwd == pwd:
        print 'welcome back', name
        if time.time()- lsttime < 4*60*60:
            print "You already logged in at:", time.ctime(lsttime)
        value[1]=time.time()
    else:
        print 'login incorrect'
    savetofile3()

def listuser():
    print "Here are the item:"
    for x in db.keys():
        print "name:%s, passwd:%s, last login time:%s" %(x, '*'*5, time.ctime(db[x][1]))

def deluser():
    name = raw_input('user name: ').lower()
    value = db.get(name)
    if value == None:
        print "The name is not exist"
        return
    db.pop(name, None)
    savetofile3()

def savetofile1():
    f = open('userprofile.txt', 'w')
    for key in db:
        f.write(key+':'+db[key][0]+":"+str(db[key][1])+os.linesep)
    f.close()

def savetofile2():
    f = open('userprofile.pickle', 'w')
    pickle.dump(db,f)
    f.close()

def readfile2():
    f = open('userprofile.pickle','r')
    global db
    db = pickle.load(f)
    f.close()

def savetofile3():
    obj = shelve.open('userprofile.shelve','c')
    obj['user'] = db
    obj.close()

def readfile3():
    obj = shelve.open('userprofile.shelve','r')
    global db
    db  = obj['user']
    obj.close()

def showmenu():
    readfile3()
    while True:
        prompt = """
        (N)ew User Login
        (E)xisting User Login
        (L)ist all users
        (D)elte a user
        (Q)uit
        Enter choice: """

        done = False
        while not done:
            chosen = False
            while not chosen:
                try:
                    choice = raw_input(prompt).strip()[0].lower()
                except (EOFError, KeyboardInterrupt):
                    choice = 'q'
                print '\nYou picked: [%s]' % choice
                if choice not in 'neqdl':
                    print 'invalid option, try again'
                else:
                    chosen = True
                    done = True
        if choice == 'n':
            newuser()
        elif choice == 'e':
            olduser()
        elif choice == 'l':
            listuser()
        elif choice == 'd':
            deluser()
        else:
            break

if __name__ == '__main__':
    showmenu()
