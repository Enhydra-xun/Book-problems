#----------------------------------------------------------------
for i in range(3,31):
	all_count=0
	list_buff=[]
	print 'sum=%d'%i
	for a in range(1,11):
		if a < i:
			for b in range(1,11):
				if a+b < i:
					for c in range(1,11):
						if i==a+b+c:
							all_count +=1
							# rate abc
							if b >= c:
								b, c = c, b
								if a >= b:
									a, b = b, a
									if b >= c:
										b, c = c, b
							list_buff.append([a,b,c])
				else:
					break
		else:
			break
	print list_buff
#	for n in range(0,len(list_buff)-1):
#		each=0
#		if list_buff[n]==list_buff[n+1]:
#			each+=1
#			del list_buff[n+1]
			#print list_buff[n], 'e_count=%d'%each

	print 'all_count=%d'%all_count
	print '\n'