import numpy as np
import math
from matplotlib import pyplot as plt 

 
x = np.arange(-1000,1000)

cond = [True if (i>400 and i<-400) else False for i in x]

t = -((x)*(x)*(x>=0) + (x)*(x)*(x<0) )/(2*300*300)

font2 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 15,
}
plt.xlabel('round',font2)
plt.ylabel('value',font2)

y =  np.exp(t)
plt.title("Gaussian function model") 
plt.xlabel("Distance frome the center") 
plt.ylabel("Brightness intensity") 
plt.plot(x,y)
plt.show()
