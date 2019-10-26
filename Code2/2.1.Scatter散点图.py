#莫烦学Python-3.1 Scatter散点图
import matplotlib.pyplot as plt
import numpy as np

n=1024
X=np.random.normal(0,1,n)								#期望为0，方差为1
Y=np.random.normal(0,1,n)
T=np.arctan2(Y,X)

plt.scatter(X,T,s=5,c=T,alpha=0.7)								#for color later on

plt.show()

 