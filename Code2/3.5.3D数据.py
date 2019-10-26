#莫烦学Python-3.5 3D数据
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()								#构建一个figure
ax=Axes3D(fig)									#通过figure绘制一个3D的坐标

#构建数据：
X=np.arange(-4,4,0.25)
Y=np.arange(-4,4,0.25)
X,Y=np.meshgrid(X,Y)
R=np.sqrt(X**2+Y**2)

Z=np.sin(R)

#ax.plot_surface(X,Y,Z)							#基础的显示
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))					#stride是行、列跨度
ax.contour(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')										#zdir=投影的轴。offset=投影的位置
ax.set_zlim(-2,2)
plt.show()