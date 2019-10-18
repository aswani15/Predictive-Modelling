# -*- coding: utf-8 -*-
from pylab import *
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import random
import re
beta = 0.4
legend_val='beta='+str(beta)
S_values=[760,738,688,536,467]
timesteps=[1,3,4,5,6]
def initialize():
    global x, result
    x = 0.1
    result = []
    
def observe():
    global x, result
    result.append(x)
    
def update(val):
    global x, result
    x = -1* beta * val * (763 - val) 
S_values = [random.randint(10,760) for _ in range(100)]
S_data = sorted(S_values, reverse=True)
initialize()
for val in S_data:    
    update(val)
    observe()
fig = plt.figure()
plt.plot( result)

fig.suptitle('Progression Of Epidemic')
plt.xlabel('day')
plt.ylabel('Incidence')
#plt.legend('β=0.2')
patch = mpatches.Patch(color='blue', label=legend_val)
plt.legend(handles=[patch])
show()