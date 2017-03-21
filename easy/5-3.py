#!/5-3
print 'input scores :'

score= input()

if score<60:
	print 'F'
elif score<69 and score>=60:
	print 'D'
elif score<79 and score>=70:
	print 'C'
elif score<89 and score>=80:
	print 'B'
elif score<=100 and score>=90:
	print 'A'