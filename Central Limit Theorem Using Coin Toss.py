#!/usr/bin/env python
# coding: utf-8

# In[32]:


import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors
from scipy import stats
import statistics
get_ipython().run_line_magic('matplotlib', 'notebook')

x = int(input("Number of times to flip coin: "))
L1=[np.random.binomial(1,0.5) for i in range(x)]
L1[1:10]


# In[34]:


n=int(input("Number of samples: "))


# In[35]:


L2=[]
for j in L1:
    np.random.seed(1)
    x = [np.mean(random.choices(L1, k=20)) for _ in range(n)]
    L2.append(x)

# plotting all the means in one figure
fig, ax = plt.subplots(2, 2, figsize =(8, 8))
for i in range(0, 2):
    for j in range(0, 2):
        # Histogram for each x stored in means
        ax[i, j].hist(L2[k], 10, density = True,edgecolor='b')
        ax[i, j].set_title(label = L1[k])
        k = k + 1
plt.show()


# In[36]:


np.random.seed(41)
q=[statistics.mean(random.sample(L1,20)) for i in range(n)]
bins=10
kde = stats.gaussian_kde(q)
xx = np.linspace(0, 1, n)
fig, ax = plt.subplots(figsize=(8,6))
ax.hist(q, density=True, bins=bins, alpha=0.3,color='b')
ax.plot(xx, kde(xx))


# In[ ]:


#clt using histogram animation 


# In[37]:


N=int(input("Number of samples: "))
L2 = [np.mean(random.choices(L1, k=20)) for _ in range(N)]
def clt(L1):
    # if animation is at the last frame, stop it
    plt.cla()
    if L1 == N: 
        a.event_source.stop()

    plt.hist(L2[0:L1],edgecolor='b')

    plt.gca().set_title('Expected value of coin toss')
    plt.gca().set_xlabel('Average from coin toss')
    plt.gca().set_ylabel('Frequency')

    plt.annotate('coin toss= {}'.format(L2), [3,27])


# In[38]:


fig= plt.figure(figsize=(8,5))
a = animation.FuncAnimation(fig, clt, interval=23)
plt.show()


# In[ ]:





# In[ ]:




