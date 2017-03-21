#!/2-8 creat a 5-num list or tuple output their addition
#!/ (2) use while / for to do
#!/2-8~2-11
print 'input a 5-num:'

x=[]
s=0
for i in range(0,5):
	x.append(input())
	s+=x[i]
print x
print 'sum is :',s
