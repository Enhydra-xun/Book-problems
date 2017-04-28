#/6-7

#
num_str = raw_input('Entera num:  ')

#
num_num = int(num_str)

#
fac_list = range(1, num_num+1)
print"Before:", fac_list

#
i=0

#
while i< len(fac_list) :

	#
	if num_num % fac_list[i] == 0 :
		del fac_list[i]

	#
	else:
		i=i+1

#
print"After:",fac_list