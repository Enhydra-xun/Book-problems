#!/
print 'input 2 nums'
a=input()
b=input()
if cmp(a,b)<0:
	c=a
else:
	c=b
for i in range(1,c+1) :
	if a%i==0 and b%i==0:
		p=i
q=a*b/p
print p
print q

