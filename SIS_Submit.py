import scipy.integrate as sci
import numpy as np
import pylab as pl

#Transmission rate
beta=0.002342
#recovery rate
alpha=0.476
#Number of observations
ND=13
#Number of susceptible people at time 1 or start of time
S0=760
#Number of Infected people at time 1 or start of time
I0=3
#initiating susceptible , Infected and time

INPUT = (S0, I0, 1.0)

#changed Transmission rate
beta=0.0026
#changed recovery rate
alpha=0.5

#actual values for comparision
actual_val=np.array([3,25,75,227,296,258,236,192,126,71,28,11,7])
#number of days
timesteps=np.array([1,3,4,5,6,7,8,9,10,11,12,13,14]    )

#Define the differential equations in this method

def diff_eqs(INP,t):
   #defining array
    Y=np.zeros((3))
   #Defining vector with time dependency
    V = INP    
   #differential equation to calculate number of susceptible individuals at given time 
    Y[0] = - beta * V[0] * V[1]
   #differential equation to calculate number of Infected individuals at given time 
    Y[1] = beta * V[0] * V[1] - alpha * V[1]    
    return Y   # For odeint

#calling odeint method from scipy library. Which integrates the given differential equation to solve the given problem
#Accepts vector and array values along with timeseries
RESULT = sci.odeint(diff_eqs,INPUT,np.array(timesteps))
print RESULT[:,1]

#Plot graph
pl.plot(timesteps,RESULT[:,1], '-ro', label='Model:Infectious')
pl.plot(timesteps,actual_val, '-go', label='Actual:Infectious')
pl.legend(loc=0)
pl.title('Model for Infected in Boarding School ')
pl.xlabel('Time')
pl.ylabel('Infectious')
pl.show()
