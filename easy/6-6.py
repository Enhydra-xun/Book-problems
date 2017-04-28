#/6-6
a=raw_input('input a str with _:\n')
alist=[]
for i in a:
	alist.append(i)
for u in range(len(alist)-1):
	if alist[0]==' ':
		del alist[0]
	else:
		break
for n in range(len(alist)-1):
	if alist[-1]==' ':
		del alist[-1]
	else:
		break
b=''
for p in range(len(alist)):
	b= b+ alist[p]

print b