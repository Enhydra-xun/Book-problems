#!/5-4
print 'input a year:',
y=input()
if ( y%4==0 and (not y%100==0) ) or y%400==0 :
	print 'run nian'
else :
	print 'not run nian'
