#!/test2.0
strr= raw_input()
num=['0','1','2','3','4','5','6','7','8','9','0']
foo=['+','-','*','#']
strr= strr+'#'
lstrr= len(strr)
a=[]
b=[]
z=''

for n in range(0,lstrr):
	if strr[n] in foo:
		b.append(strr[n])
	elif strr[n] in num:
		z= z+ strr[n]
		if strr[n+1] in foo:
			a.append(z)
			z=''

sumall=a[0]
la=len(a)
for u in range(0,la-1):
	sumall=sumall+b[u]+a[u+1]
	sumall=eval(sumall)

print sumall