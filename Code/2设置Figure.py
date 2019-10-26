#莫烦学Python-2.2 figure图像
		#一个figure相当于一个画布

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,20)		#从-3到3均分出20个点
y1=2*x+1
y2=x**2

plt.figure()		
plt.plot(x,y1)		#属于figure1


plt.figure(num=3,figsize=(8,5))				#可以定义画布的编号，尺寸
plt.plot(x,y2,color='red',linewidth=1,linestyle='--')		#属于figure2		可以定义线条的颜色，宽度，样式

plt.show()
