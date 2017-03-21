#!/5-6
from __future__ import division
print 'N1 [] N2 :',
s=0
str=raw_input()
N1,foo,N2=str.split(' ',2)
N1=int(N1)
N2=int(N2)
if foo=='+':
	s=N1+N2
elif foo=='-':
	s=N1-N2
elif foo=='*':
	s=N1*N2
elif foo=='^':
	s=pow(N1,N2)
elif foo=='/':
	s=N1/N2
elif foo=='%':
	s=N1%N2

print str,'=',s