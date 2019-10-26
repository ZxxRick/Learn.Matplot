#莫烦学Python-2.6 Annotation标注
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
###################################################################################


#设置想要标注点：
x0=1
y0=2*x0+1
plt.scatter(x0,y0,s=35,color='r')					#将点通过scatter标注出来     scatter：散播，散布于
plt.plot([x0,x0],[y0,0],'r--',lw=2.5)				#设置直线的两点为[x0,y0],[x0,0],'r--'指的是red颜色和--格式。lw指宽度







plt.show()


