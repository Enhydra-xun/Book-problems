#!/usr/bin/env python

def displayNumType(num):
	print num,'is',
	if isinstance(num, (int,long,float,complex,str)):  # isinstance(num,(#all types that fit in)):
		print 'a number of type:',type(num).__name__
	else:
		print 'not a number at all!'

displayNumType(-69)
displayNumType(9999999999999)
displayNumType(98.67)
displayNumType(-5.2+1.9j)
displayNumType('xxx')
