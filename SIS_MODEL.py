# -*- coding: utf-8 -*-
from pylab import *
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from decimal import *
import re


    
def calculateinfected(i,alpha,beta,previous,n): 
    #p=float(i)/float(n )   
    y = ((beta*i)*(n-i))-(alpha*(i) )
    #p=3*(math.exp(-1*alpha*t))
    #y = previous+(((alpha*p)*(1-p))-(beta*(p) )*t)
    return y
beta = 0.002342
legend_val='beta='+str(beta)
alpha=0.476
I_values=[3,25,75,227,296,192,126,71]
I=[3,25,75,227,296,192,126,71]
result=[]
result_prev=[0,3,25,75,227,296,192,126]
timesteps=[1,3,4,5,6,7,8,9]    
y=0
previous=0
n=763
q=0
for val in I:    
    y=calculateinfected(val,alpha,beta,result_prev[q],n)
    result.append(y)
    q=q+1
    
fig = plt.figure()
plt.plot(timesteps,result,color='skyblue')
plt.plot(timesteps,I_values,color='green')
fig.suptitle('Number of Infected')
plt.xlabel('day')
plt.ylabel('Number of Infected')
#plt.legend('β=0.2')
patch = mpatches.Patch( label="blue: Model , Green: Actual")
plt.legend(handles=[patch])
show()