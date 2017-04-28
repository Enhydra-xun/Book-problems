#
for i in range(3,31):
	all_count=0
	print 'sum=%d'%i
	for a in range(1,11):
		if a < i:
			for b in range(1,11):
				if a+b < i:
					for c in range(1,11):
						if a+b+c==i:
							all_count +=1
							print '%d, %d, %d' %(a,b,c)
				else:
					break
		else:
			break
	print 'all_count=%d\n'%(all_count)