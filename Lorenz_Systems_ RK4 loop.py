#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 09:29:40 2022

@author: ksxuphy
"""

import numpy as np #For arrays
import matplotlib.pyplot as plt #For plotting

sigma = 10.0 #Variable for dx/dt
rho = 28.0 #Variable for dy/dt
beta = 8/3 #Variable for dz/dt
t = 0 #Starting time
tf = 40 #Ending time
h = 0.01 #Step size for RK4
#These variables were used since they can be easily found for comparison, for example, in Wikipedia under the Lorenz system article



#Derivative function to work with RK4 loop
def derivative(r,t):
    x = r[0]
    y = r[1]
    z = r[2]
    return np.array([sigma * (y - x), x * (rho - z) - y, (x * y) - (beta * z)])




time = np.array([]) #Empty time array to fill for the x-axis
x = np.array([]) #Empty array for x values
y = np.array([]) #Empty array for y values
z = np.array([]) #Empty array for z values
r = np.array([1.0, 1.0, 1.0]) #Initial conditions array


while (t <= tf ):
        #Appending values to graph
        time = np.append(time, t)
        z = np.append(z, r[2])
        y = np.append(y, r[1])
        x = np.append(x, r[0])
        #RK4 Step method
        k1 = h*derivative(r,t)
        k2 = h*derivative(r+k1/2,t+h/2)
        k3 = h*derivative(r+k2/2,t+h/2)
        k4 = h*derivative(r+k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6
        #Updating time value with step size
        t = t + h
        
        
        
#Multiple graph plotting
fig, (ax1,ax2,ax3) = plt.subplots(1,3, figsize = (15, 5))
ax1.plot(x, y)
ax1.set_title("X & Y")
ax2.plot(x, z)
ax2.set_title("X & Z")
ax3.plot(y, z)
ax3.set_title("Y & Z")
plt.show()