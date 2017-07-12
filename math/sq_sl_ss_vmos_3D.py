#/	ss,sq,sl,vmos		in 3D
import numpy as np
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm 
from matplotlib.ticker import LinearLocator

csvFile = open('SpeedVideoDataforModeling.csv','r')
csv_reader = csv.reader(csvFile)

all_data = []

for item in csv_reader:
	CVB_y = [	float(item[16]),
				float(item[14]), 
			 	float(item[15]),
			 	float(item[6])	]
	all_data.append(CVB_y)

all_data = np.array(all_data)

p, x, y, z = all_data[:,0], all_data[:,1], all_data[:,2], all_data[:,3]

fig = plt.figure()
ax=plt.subplot(111,projection='3d') 	#bulid a 3D project

#draw 3D plot
#sperated in 3 parts which in diff colors
#ax.scatter(x[:1000],y[:1000],z[:1000],c='b') 
#ax.scatter(x[1000:4000],y[1000:4000],z[1000:4000],c='m')
#ax.scatter(x[4000:],y[4000:],z[4000:],c='g')
ax.scatter(x,y,z)

#cordines
#ax.set_xlabel('sStalling')
ax.set_ylabel('sQuality')
ax.set_ylabel('sLoading')
ax.set_zlabel('vMOS')
plt.show()



