#/6-8

#	1 ~ 9
def turn1(n):
	direct1={1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'serven' ,8:'eight', 9:'nine'}
	return direct1[n]

#	11 ~ 19
def turn2(n):
	direct2={1:'eleven', 2:'twelve', 3:'thirteen', 4:'forteen', 5:'fifteen',6:'sixteen', 7:'severteen', 8:'eighteen', 9:'nighteen'}
	return direct2[n]

#	x0
def turn3(n):
	direct3={1:'ten', 2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
	return direct3[n]

if __name__ == '__main__':
	for num in range(0,1001):
	#	num = input('input a num in 0~1000:\n')
		nlist=[]
		for u in str(num):
			nlist.append(u)
	#?
		if 0<=num<10:
			if num ==0:
				print 'zero'
			else:
				return_value= turn1(num)
				print return_value
	#??
		elif 10<=num<100:
	#	?0
			if nlist[1]=='0':
				n_ten = turn3(int(nlist[0]))
				print n_ten
	#	1x
			elif 9<num<20:
				n_omg = turn2(int(nlist[1]))
				print n_omg
	#	xx
			elif 20<num<100:
				n_ten = turn3(int(nlist[0]))
				n_omg = turn1(int(nlist[1]))
				print n_ten,'-',n_omg
	#???
		elif 100<=num<1000:
			n_hun = turn1(int(nlist[0]))
	#	x0?
			if nlist[1]=='0':
	#		x00
				if nlist[2]=='0':
					print n_hun,' hundred'
	#		x0x
				else:
					n_omg = turn1(int(nlist[2]))
					print n_hun,' hundred and ',n_omg
	#	xx0
			elif nlist[2]=='0':
					n_ten = turn3(int(nlist[1]))
					print n_hun,' hundred and ',n_ten
	#	x?x
			else:
	#		x1x
				if nlist[1]=='1':
					n_omg = turn2(int(nlist[2]))
					print n_hun,' hundred and ',n_omg
	#		xxx
				else:
					n_ten = turn3(int(nlist[1]))
					n_omg = turn1(int(nlist[2]))
					print n_hun,' hundred and ',n_ten,'-',n_omg
	#1000
		elif num==1000:
			print 'one thousand'

