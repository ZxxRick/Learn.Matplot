#莫烦学Python-2.4 设置坐标轴2
import matplotlib.pyplot as plt
import numpy as np

###################################################################################
#2.3节课的代码
x=np.linspace(-3,3,250)		#从-3到3均分出50个点
y1=2*x+1
y2=x**2


plt.figure()			
plt.plot(x,y1)
plt.plot(x,y2,color='red',linewidth=1,linestyle='--')	#可以定义线条的颜色，宽度，样式
###################################################################################

#将坐标轴设置为正常见的
#gca='get current axis'								#获取当前的这四个轴
ax=plt.gca()
ax.spines['right'].set_color('none')				#将右边的框设置为none
ax.spines['top'].set_color('none')					#将上边的框设置为none

ax.xaxis.set_ticks_position('bottom')				#将底部脊梁作为x轴
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))		#设置x轴的位置(设置底的时候依据的是y轴)
ax.spines['left'].set_position(('data',0))			#设置左脊梁(y轴)依据的是x轴的0位置


plt.show()


