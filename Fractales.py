#!/usr/bin/env python
# coding: utf-8

# # 1)

# In[ ]:


import random
import matplotlib.pyplot as plt
ordonnes = []
abscisses = []
x=0.5
y=0
for i in range(30000):
    p=random.uniform(0,1)
    if p<0.1:
        xn=0.05*x 
        yn=0.6*y
    elif 0.1<p<0.2:
        xn=0.05*x
        yn=-0.5*y+1
    elif 0.2<p<0.4:
        xn=0.46*x-0.32*y
        yn=0.39*x+0.38*y+0.6
    elif 0.4<p<0.6:
        xn=0.47*x-0.15*y
        yn=0.17*x+0.42*y+1.1
    elif 0.6<p<0.8:
        xn=0.34*x+0.28*y
        yn=-0.25*x+0.45*y+1
    else:
        xn=0.42*x+0.26*y
        yn=-0.35*x+0.31*y+0.7
    x=xn
    y=yn
    ordonnes += [yn]
    abscisses += [xn]
ax = plt.gca()
ax.set_xticks([])
ax.set_yticks([])
plt.plot(abscisses, ordonnes, "g.")
plt.show()


# # 2)

# In[ ]:


import random
import matplotlib.pyplot as plt
ordonnes = []
abscisses = []
x=0.05
y=0
for i in range(30000):
    p=random.uniform(0,100)
    if p<2:
        xn=0.5
        yn=0.27*y
    elif 2<p<17:
        xn=-0.139*x+0.263*y+0.57
        yn=0.246*x+0.224*y-0.036
    elif 17<p<30:
        xn=0.17*x-0.215*y+0.408
        yn=0.222*x+0.176*y+0.0893
    elif 30<p<100:
        xn=0.781*x+0.034*y-0.1075
        yn=-0.032*x+0.739*y+0.27
    x=xn
    y=yn
    ordonnes += [yn]
    abscisses += [xn]
ax = plt.gca()
ax.set_xticks([])
ax.set_yticks([])
plt.plot(abscisses, ordonnes, "r.")
plt.show()


# 
# # 3)

# In[ ]:


import random
import matplotlib.pyplot as plt
x=[1,3,5,3,1]
y=[1,1,1,5,1]
plt.plot(x, y, "y")
plt.show()
plt.close()

