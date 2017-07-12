#	modle1_2D
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
	CVB_y = [	float(item[13]), 
				float(item[12]), 
				float(item[4]),
				float(item[6])		]
	all_data.append(CVB_y)

all_data = np.array(all_data)

#print type(all_data)

fig = plt.figure()
ax = fig.add_subplot(111)

z, x, y, p = all_data[:,0], all_data[:,1], all_data[:,2], all_data[:,3]

ax.scatter(x, y,)

#ax.set_xlabel('sStalling')
#ax.set_xlabel('Sa')
ax.set_xlabel('k')
ax.set_ylabel('ta')
plt.show()