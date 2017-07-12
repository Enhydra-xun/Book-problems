#	Sa_ta_k	in 3D

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
	Satak = [	float(item[4]),			#	ta
				float(item[12]), 		#	k
			 	float(item[13]),	]	#	Sa
	all_data.append(Satak)

all_data = np.array(all_data)
x, y, z = all_data[:,0]/10000, all_data[:,1], all_data[:,2]/1000000

fig = plt.figure()
ax=plt.subplot(111,projection='3d') 	#bulid a 3D project

ax.scatter(x,y,z)

#cordines
ax.set_xlabel('ta *10^10000')
ax.set_ylabel('k')
ax.set_zlabel('Sa *10^6')
plt.show()
