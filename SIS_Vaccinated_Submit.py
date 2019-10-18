import scipy.integrate as sci
import numpy as np
import pylab as pl

#Transmission rate
beta=0.002342
#recovery rate
alpha=0.476

#vaccination rate initiate to value
mu=0.4
#Number of observations
ND=13
#Number of susceptible people at time 1 or start of time
S0=760
#Number of Infected people at time 1 or start of time
I0=3
#initiating susceptible , Infected and time
INPUT = (S0, I0, 1.0)

timesteps=np.array([1,3,4,5,6,7,8,9,10,11,12,13,14]    )
#Define the differential equations in this method
def diff_eqs(INP,t):
    #defining array
    Y=np.zeros((2))
    #Defining the array of vector with time dependency
    V = INP    
    #differential equation to calculate number of susceptible individuals at given time
    Y[0] = - beta * V[0] * V[1]
   #differential equation to calculate number of susceptible individuals at given time
    Y[1] = beta * V[0] * V[1] - alpha * V[1]- mu * V[1]   
    return Y   

#calling odeint method from scipy library. Which integrates the given differential equation to solve the given problem
#Accepts vector and array values along with timeseries
RESULT = sci.odeint(diff_eqs,INPUT,np.array(timesteps))
print (RESULT[:,1])

#Plot graph

pl.plot(timesteps,RESULT[:,1], '-ro', label='Model:Infectious with mu = 0.4')
#pl.plot(timesteps,actual_val, '-go', label='Actual:Infectious')
pl.legend(loc=0)
pl.title('Model for Infected in Boarding School including Vaccinated')
pl.xlabel('Time')
pl.ylabel('Infectious')
pl.show()
