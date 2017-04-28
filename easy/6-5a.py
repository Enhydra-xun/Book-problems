#6-5
a= raw_input('input a string')
alist=[]
for eachstr in a:
	alist.append(eachstr)

for u in range(len(alist)-1):
	print alist[u-1], alist[u], alist[u+1],'\n'
	