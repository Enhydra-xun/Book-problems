#	rate abc
def tri_rate(ac,bc,cc):
	if bc > cc :
		bc, cc = cc, bc
		if ac > bc :
			ac, bc =bc, ac
	return [ac,bc,cc]

if '__name__'=='__main__':
#----------------------------------------------------------------
	for i in range(3,31):
		count=0
		list_buff=[]
		print 'sum=%d'%i
		for a in range(1,11):
			if a < i:
				for b in range(1,11):
					if a+b < i:
						for c in range(1,11):
							if i==a+b+c:
								count +=1
								#add abc in to list
								tri_rate(a,b,c)
								list_buff.append(return_value)
	#count abc which are the same			
	for each in range(len(list_buff)):
		count_eacheq=1
		if list_buff[each]==list_buff[each+1]:
			count_eacheq+=1
			del list_buff[each+1]
			blist=[list_buff,count_eacheq]
			print blist

