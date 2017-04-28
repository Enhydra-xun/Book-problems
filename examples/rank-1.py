#rank!

a= raw_input("input a list of num with ',' to spit:\n")
num= []
for i in a.split(','):
	num.append(int(i))

for n in range(len(num)):
	for u in range(1,len(num)-1):
		if num[u]<num[u-1]:
			num[u-1],num[u]= num[u],num[u-1]

print num