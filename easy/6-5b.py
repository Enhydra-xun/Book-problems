#/6-5b

import string

astr= raw_input('import string-a:	')
bstr= raw_input('import string-b:	')

if astr.find(bstr)== -1:
	print 'No found'
else:
	print astr.find(bstr)
