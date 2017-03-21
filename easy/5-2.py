#!/5-2
print 'input two num'
def foo1():
	a= int(raw_input())
	b= int(raw_input())
	print a*b

def foo2(a,b):
	print a*b

def foo3():
	a= input()
	b= input()
	return a*b

if __name__== '__main__':
	print 'executing foo1:'
	foo1()

	print 'executing foo2:'
	foo2(2,3)

	print 'executing foo3:'
	return_value = foo3()
	print return_value
