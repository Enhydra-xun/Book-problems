#!/thinking problems
import random
N=random.randint(2,101)
aList=[]
for i in range (1,N):
	n= random.randint(1, 2**31)
	aList.append(n)
print 'aList0:', aList

bList=[]
for p in range (1,N):
	u= random.choice(aList)
	bList.append(u)
print 'bList1:',bList

for q in range(len(bList),0,-1):
	for s in range (0,q-1):
		if bList[s] > bList[s+1]:
			bList[s],bList[s+1] = bList[s+1],bList[s]

print 'bList2:', bList






