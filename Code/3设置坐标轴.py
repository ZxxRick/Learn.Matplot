#莫烦学Python-2.3 设置坐标轴
import matplotlib.pyplot as plt
import numpy as np

###################################################################################
#上节课的代码
x=np.linspace(-3,3,250)		#从-3到3均分出50个点
y1=2*x+1
y2=x**2

plt.figure()			
plt.plot(x,y1)
plt.plot(x,y2,color='red',linewidth=1,linestyle='--')	#可以定义线条的颜色，宽度，样式
###################################################################################

plt.xlim((-1,2))		#更改轴的长度
plt.ylim((-2,3))
plt.xlabel("this X")	#添加label
plt.ylabel("this Y")		

new_ticks=np.linspace(-1,2,5)
plt.xticks(new_ticks)					#更改轴的区间段？？？（说不清）
plt.yticks([-2,-1.8,-1,1.22,3],
		   ["td","d","n","g","$t\ g$"])		#更改轴的标识  $改字体样式




plt.show()

