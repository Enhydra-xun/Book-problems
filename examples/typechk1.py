def displayNumType(num):
	import types                             # can also written as|| from types import IntType ; if  type(num) is IntType: ||
	if type(num) is types.IntType:           # all compare to the type'int'
		print num,'is',type(num).__name__
	else:
		print num,'is not Int'

displayNumType(-69)
displayNumType(9999999999999)
displayNumType(98.67)
displayNumType(-5.2+1.9j)
displayNumType('xxx')
