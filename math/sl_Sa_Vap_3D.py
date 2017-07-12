#	sl_Sa_Vap_3D

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
	vap = float(item[13])/(float(item[4])-float(item[2]))
	SaVapsl = [float(item[13]),vap,float(item[15])]
	all_data.append(SaVapsl)

all_data = np.array(all_data)
x, y, z = all_data[:,0]/1000000, all_data[:,1]/1000, all_data[:,2]

fig = plt.figure()
ax=plt.subplot(111,projection='3d') 	#bulid a 3D project

ax.scatter(x,y,z)

#cordines
ax.set_xlabel('Sa *10^6')
ax.set_ylabel('|Va| *10^3')
ax.set_zlabel('sLoading')
plt.show()
