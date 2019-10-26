#莫烦学Python-2.5 设置图例
import matplotlib.pyplot as plt
import numpy as np

###################################################################################
#2.3节课的代码
x=np.linspace(-3,3,250)		#从-3到3均分出50个点
y1=2*x+1
y2=x**2

plt.figure()			
plt.plot(x,y1,label='A')
plt.plot(x,y2,label='B',color='red',linewidth=1,linestyle='--')	#可以定义线条的颜色，宽度，样式
###################################################################################

#plt.legend()				#添加图例。   注：已经在plt.plot()中设置过label
plt.legend(loc='best',shadow = True)
"""legend( handles=(line1, line2, line3),
           labels=('label1', 'label2', 'label3'),
           'upper right')
    shadow = True 设置图例是否有阴影
    The *loc* location codes are::
          'best' : 0,         
          'upper right'  : 1,
          'upper left'   : 2,
          'lower left'   : 3,
          'lower right'  : 4,
          'right'        : 5,
          'center left'  : 6,
          'center right' : 7,
          'lower center' : 8,
          'upper center' : 9,
          'center'       : 10,"""

plt.show()


