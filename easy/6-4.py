#6-4
from __future__ import division
a= raw_input("input scores(with ','):\n")
score=[]
for i in a.split(','):
	score.append(int(i))

for u in range(len(score)):
	if score[u]<60:
		print 'F'
	elif score[u]<69 and score[u]>=60:
		print 'D'
	elif score[u]<79 and score[u]>=70:
		print 'C'
	elif score[u]<89 and score[u]>=80:
		print 'B'
	elif score[u]<=100 and score[u]>=90:
		print 'A'

average= sum(score)/(len(score))
print average