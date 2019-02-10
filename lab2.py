
# coding: utf-8

# In[3]:


import math
import numpy as np
def mean_num_friends(x):
    # TODO
    return np.mean(x)

def median_num_friends(x):
    # TODO
    return np.median(x)

num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]

print("mean={}".format(mean_num_friends(num_friends)))

print("median={}".format(median_num_friends(num_friends)))



# In[4]:


def normal_pdf(x, mu=0, sigma=1):
    r = (1/math.sqrt(2*3.14*(sigma*sigma))*math.exp((-1*((x-mu)*(x-mu))/(2*sigma*sigma))))
    return r

from matplotlib import pyplot as plt
xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '-', label='mu=0,sigma=2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], '-', label='mu=0,sigma=0.5')
plt.plot(xs, [normal_pdf(x, sigma=-1) for x in xs], '-', label='mu=0,sigma=-1')
plt.legend()
plt.show()

