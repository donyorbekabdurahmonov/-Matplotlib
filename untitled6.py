# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Xah248kdhGZo7CLLefM3XmXq7XiYo1yN
"""

import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,1,2,3,4,5])
y=np.array([0,8,12,20,26,38])

plt.scatter(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,0,5,5,5,0,2,2,1,1,3,3,4,4,0,0,0,0,5,5,5,5])
y=np.array([5,35,35,5,20,20,35,5,35,5,35,5,35,5,10,15,25,30,10,15,25,30])

plt.scatter(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,1,2,3,4,5])
y=np.array([0,2,8,1,14,7])

mycolor=['red','green','purple','lime','aqua','yellow']
size=[10,60,120,80,20,190]

plt.scatter(x,y,color=mycolor,s=size)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,1,2,3,4,5])
y=np.array([0,2,8,1,14,7])

mycolor=['red','green','purple','lime','aqua','yellow']
size=[10,60,120,80,20,190]

plt.scatter(x,y,color=mycolor,s=size,alpha=0.3)
plt.show()