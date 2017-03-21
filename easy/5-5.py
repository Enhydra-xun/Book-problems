#!/ qu yu
print 'input a num <100 :',
m=int(raw_input())
a0= m/25
a1= m%25
b0= a1/10
b1= a1%10
c0= b1/5
c1= b1%5

print '%d = %d [25$]; %d [10$]; %d [5$]; %d [1$]' %(m,a0,b0,c0,c1)