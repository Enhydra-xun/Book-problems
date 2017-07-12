#	work_out_|Va|=Vap

import csv
import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator

csvFile = open('SpeedVideoDataforModeling.csv','r')
csv_reader = csv.reader(csvFile)

all_data = []

for item in csv_reader:
	vap = float(item[13])/(float(item[4])-float(item[2]))
	VVaVap = [float(item[3]),float(item[1]),vap]
	all_data.append(VVaVap)

all_data = np.array(all_data)

print all_data
x = all_data[:,0]/10000
y = all_data[:,1]/10000
z = all_data[:,2]/1000

fig = plt.figure()
ax=plt.subplot(111,projection= '3d')
ax.scatter(x,y,z)
ax.set_xlabel('V *10^4')
ax.set_ylabel('Va *10^4')
ax.set_zlabel('|Va| *10^3')
plt.show()