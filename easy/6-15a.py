#/6-15a

import string
dirct={'01':334, '02':306, '03':275, '04':245, '05':214, '06':184, '07':153, '08':122, '09':92, '10':61, '11':31, '12':0}

in1=raw_input('input date-1(DD/MM/YY):	')
in2=raw_input('input date-2(DD/MM/YY):	')

date1=in1.split('/')
date2=in2.split('/')

if int(date1[2])>int(date2[2]):
	date1,date2 = date2,date1
elif int(date1[2])==int(date2[2]):
	if int(date1[1])>int(date2[1]):
		date1,date2 = date2,date1
	elif int(date1[1])==int(date2[1]):
		if int(date1[0])>int(date2[0]):
			date1,date2 = date2,date1

dy= int(date2[2])-int(date1[2])

dd1= dirct[date1[1]]-int(date1[0])
dd2= dirct[date2[1]]-int(date2[0])

alldays= dd1-dd2+dy*365
print alldays
