#		

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(0, 4, 0.05)
Y = np.arange(0, 4, 0.05)

X, Y = np.meshgrid(X, Y)

a = 0.225511
b = 0.957617
c = -4.138842

Z = a*X**2 + b*Y + c 
ax.set_xlabel('ss') 
ax.set_ylabel('sl')
ax.set_zlabel('vmos')

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

plt.show()