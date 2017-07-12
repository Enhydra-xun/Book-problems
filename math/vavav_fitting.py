#	


from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(0, 100, 1)
Y = np.arange(0, 100, 1)

X, Y = np.meshgrid(X, Y)

a = -2.22E-07
b = 0.053171
c = -2.00E-05
d = 0.261877
e = -2.72E-06
f = -410.6467

Z = a*X**2 + b*X + c*Y**2 + d*Y + e*X*Y + f 

ax.set_xlabel('Va') 
ax.set_ylabel('V')
ax.set_zlabel('Vap')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

plt.show()