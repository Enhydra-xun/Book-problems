#!/usr/bin/env python

'makeTextFile.py-- creat text file'

import os
ls= os.linesep

# get filename
while True:

    if os.path.exists(fname):
        print "error: '%s' already exists" %fname
    else:
        break

#get file content(text)lines
all =[]
print "\nEnter lines('.' by itself to quit).\n"

#loop until user terminates input
while True:
    entry=raw_input('>')
    if entry=='.':
        break
    else:
        all.append(entry)

#write lines to file with proper line-ending
fobj=open(fname,'w')
fobj.writelines(['%s%s' %(x,ls) for x in all])
fobj.close()
print 'Done!'
