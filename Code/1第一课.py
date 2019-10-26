#莫烦学Python-2.1基本用法

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-1,1,20)		#从-1到1 均分出20个点
y=2*x+1

plt.plot(x,y)
plt.show()
