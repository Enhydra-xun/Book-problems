#/6-5d
import string
a= raw_input('import a str')

alist=[]
for u in a:
	alist.append(u)

for n in range(len(a)/2):
	alist[n],alist[len(a)-1-n]= alist[len(a)-1-n],alist[n]
b=''
for i in range(len(a)):
	a= a+alist[i]
print a