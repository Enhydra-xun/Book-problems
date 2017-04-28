#!/only 0~9  & +,-,*
strr=raw_input()
i=len(strr)

for n in range(0,i-1,2):
	a=str(s)+strr[n+1:n+3]
	s=eval(a)
print s
