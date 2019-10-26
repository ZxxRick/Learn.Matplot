#莫烦学Python-3.2 Bar柱状图
import matplotlib.pyplot as plt
import numpy as np

n=12
X=np.arange(n)
Y1=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2=(1-X/float(n))*np.random.uniform(0.5,1.0,n)


plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white')				#设置主体的颜色值、外框的颜色值
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')

for x,y in zip(X,Y1):
	#ha:horizontal alignment
	plt.text(x,y+0.05,'%.2f'%y,ha='center',va='bottom')


for x,y in zip(X,-Y2):
	#ha:horizontal alignment
	plt.text(x,y-0.1,'-%.2f'%y,ha='center',va='bottom')


plt.show()

 
