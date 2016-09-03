#!/usr/bin/env python 
#coding = gbk
from urllib import urlretrieve

def firstNonBlank(lines):
    for eachLine in lines:
        if not eachLine.strip():
            continue
        else:
            return eachLine

def firstLast(webpage):
    f = open(webpage)
    lines = f.readlines()
    f.close()
    print firstNonBlank(lines),
    lines.reverse()
    print firstNonBlank(lines),

def printalllines(webpag):
    f = open(webpag)
    lines = f.readlines()
    f.close()
    for line in lines:
        print line,

def download(url='http://www.163.com',process=printalllines):
    try:
        retval = urlretrieve(url)[0]

    except IOError:
        retval = None
    if retval:  # do some processing
        process(retval)

if __name__ == '__main__':
    download()