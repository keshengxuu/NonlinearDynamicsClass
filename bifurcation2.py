#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 13:40:13 2021

@author: ksxuphy
"""
from numpy import *
import matplotlib.pyplot as plt
#% matplotlib inline

# prepare plot
fig = plt.figure(1,figsize=(9,6))
ax1 = fig.add_subplot(1, 1, 1)

# stable equilibrium
def xeq1(r):
    return sqrt(r)

# unstable equilibrium
def xeq2(r):
    return -sqrt(r)


domain = linspace(0, 10)
ax1.plot(domain, xeq1(domain), 'b-', label = 'stable equilibrium', linewidth = 3)
ax1.plot(domain, xeq2(domain), 'r--', label = 'unstable equilibrium', linewidth = 3)
ax1.legend(loc='upper left')
#neutral equilibrium point
ax1.plot([0], [0], 'go')
ax1.axis([-10, 10, -5, 5])
ax1.set_xlabel('r')
ax1.set_ylabel('x_eq')
ax1.set_title('Saddle-node bifurcation')

#black arrows indicating the attracting dynamics of the stable and the repelling dynamics of the unstable equilibrium point: 
ax1.annotate('', xy=(-7, -4), xytext=(-7, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate('', xy=(-5, -4), xytext=(-5, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate('', xy=(-3, -4), xytext=(-3, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate('', xy=(-1, -4), xytext=(-1, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate('', xy=(1, -4), xytext=(1, -1.5), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate('', xy=(1, 0.7), xytext=(1, -0.7), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate('', xy=(1, 1.5), xytext=(1, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate('', xy=(3, -4), xytext=(3, -2), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate('', xy=(3, 1.5), xytext=(3, -1.5), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate('', xy=(3, 2), xytext=(3, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate('', xy=(5, -4), xytext=(5, -2.5), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate('', xy=(5, 2), xytext=(5, -2), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate('', xy=(5, 2.5), xytext=(5, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate('', xy=(7, -4), xytext=(7, -3), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate('', xy=(7, 2.3), xytext=(7, -2.3), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate('', xy=(7, 3), xytext=(7, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)


# stable equilibrium > 0
def xeq1(r):
    return r

# unstable equilibrium > 0
def xeq2(r):
    return r - r  # = 0

# prepare plot
fig = plt.figure(2,figsize=(9,6))

domain1 = linspace(-10, 0)
domain2 = linspace(0, 10)
plt.plot(domain1, xeq1(domain1), 'r--', linewidth = 3)
plt.plot(domain1, xeq2(domain1), 'b-', linewidth = 3)
plt.plot(domain2, xeq1(domain2), 'b-', linewidth = 3)
plt.plot(domain2, xeq2(domain2), 'r--', linewidth = 3)
#neutral equilibrium point
plt.plot([0], [0], 'go')
plt.axis([-10, 10, -10, 10])
plt.xlabel('r')
plt.ylabel('x_eq')
plt.title('Transcritical bifurcation')

#black arrows: 
plt.annotate('', xy=(0, -1), xytext=(0, -9), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(0, 1), xytext=(0, 9), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(-5, -1), xytext=(-5, -4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(-5, 1), xytext=(-5, 9), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(-5, -9), xytext=(-5, -6), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(5, 4), xytext=(5, 1), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(5, -9), xytext=(5, -1), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(5, 6), xytext=(5, 9), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)


fig = plt.figure(3,figsize=(9,6))
# 1 equilibrium
def xeq1(r):
    return r - r      # = 0

# 2 equilibrium
def xeq2(r):
    return sqrt(r)

# 3 equilibrium
def xeq3(r):
    return -sqrt(r)

domain1 = linspace(-10, 0)
domain2 = linspace(0, 10)
plt.plot(domain1, xeq1(domain1), 'b-', linewidth = 3)
plt.plot(domain2, xeq1(domain2), 'r--', linewidth = 3)
plt.plot(domain2, xeq2(domain2), 'b-', linewidth = 3)
plt.plot(domain2, xeq3(domain2), 'b-', linewidth = 3)
#neutral equilibrium point
plt.plot([0], [0], 'go')
plt.axis([-10, 10, -5, 5])
plt.xlabel('r')
plt.ylabel('x_eq')
plt.title('Supercritical pitchfork bifurcation')

#black arrows: 
plt.annotate('', xy=(0, -1), xytext=(0, -4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(0, 1), xytext=(0, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(-5, -0.5), xytext=(-5, -4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(-5, 0.5), xytext=(-5, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(3, 1.5), xytext=(3, 0.5), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(3, -1.5), xytext=(3, -0.5), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(3, 2.2), xytext=(3, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(3, -2.2), xytext=(3, -4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(7, 2), xytext=(7, 0.5), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(7, -2), xytext=(7, -0.5), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(7, 3), xytext=(7, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(7, -3), xytext=(7, -4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)


fig = plt.figure(4,figsize=(9,6))
# 1 equilibrium
def xeq1(r):
    return r - r      # = 0

# 2 equilibrium
def xeq2(r):
    return sqrt(-r)

# 3 equilibrium
def xeq3(r):
    return -sqrt(-r)

domain1 = linspace(-10, 0)
domain2 = linspace(0, 10)
plt.plot(domain1, xeq1(domain1), 'b-', linewidth = 3)
plt.plot(domain1, xeq2(domain1), 'r--', linewidth = 3)
plt.plot(domain1, xeq3(domain1), 'r--', linewidth = 3)
plt.plot(domain2, xeq1(domain2), 'r--', linewidth = 3)
#neutral equilibrium point
plt.plot([0], [0], 'go')
plt.axis([-10, 10, -5, 5])
plt.xlabel('r')
plt.ylabel('x_eq')
plt.title('Subcritical pitchfork bifurcation')

#black arrows: 
plt.annotate('', xy=(1, -4), xytext=(1, -1), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(1, 4), xytext=(1, 1), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(5, -4), xytext=(5, -0.5), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(5, 4), xytext=(5, 0.5), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(-3, 0.5), xytext=(-3, 1.5), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(-3, -0.5), xytext=(-3, -1.5), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(-3, 4), xytext=(-3, 2.2), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(-3, -4), xytext=(-3, -2.2), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(-7, 0.5), xytext=(-7, 2), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(-7, -0.5), xytext=(-7, -2), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(-7, 4), xytext=(-7, 3), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(-7, -4), xytext=(-7, -3), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)



fig = plt.figure(5,figsize=(9,6))
# 1 equilibrium
def xeq1(r):
    return -r + r**3

domain1 = linspace(-1.3, -sqrt(1/3.))
domain2 = linspace(-sqrt(1/3.), sqrt(1/3.))
domain3 = linspace(sqrt(1/3.), 1.3)
plt.plot(xeq1(domain1), domain1, 'b-', linewidth = 3)
plt.plot(xeq1(domain2), domain2, 'r--', linewidth = 3)
plt.plot(xeq1(domain3), domain3, 'b-', linewidth = 3)
plt.axis([-1, 1, -1.5, 1.5])
plt.xlabel('r')
plt.ylabel('x_eq')
plt.title('Combination of two saddle-node bifurcations')

plt.annotate('', xy=(0.75, 1.2), xytext=(0.75, -1.4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(0.5, 1.1), xytext=(0.5, -1.4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(0.5, 1.25), xytext=(0.5, 1.4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(0.25, -0.9), xytext=(0.25, -1.4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(0.25, -0.8), xytext=(0.25, -0.3), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(0.25, 1), xytext=(0.25, -0.1), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(0.25, 1.15), xytext=(0.25, 1.4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(0, -1.05), xytext=(0, -1.4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(0, -0.9), xytext=(0, -0.1), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(0, 0.9), xytext=(0, 0.1), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(0, 1.05), xytext=(0, 1.4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(-0.75, -1.2), xytext=(-0.75, 1.4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(-0.5, -1.1), xytext=(-0.5, 1.4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(-0.5, -1.25), xytext=(-0.5, -1.4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(-0.25, 0.9), xytext=(-0.25, 1.4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(-0.25, 0.8), xytext=(-0.25, 0.3), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(-0.25, -1), xytext=(-0.25, 0.1), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate('', xy=(-0.25, -1.15), xytext=(-0.25, -1.4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)




dt = 0.01

# prepare plots
fig = plt.figure(6,figsize=(18,6))

def plot_phase_space():
    x = y = 0.1
    xresult = [x]
    yresult = [y]
    for t in range(10000):
        nextx = x + y * dt
        nexty = y + (-r * (x**2 - 1) * y - x) * dt
        x, y = nextx, nexty
        xresult.append(x)
        yresult.append(y)
    plt.plot(xresult, yresult)
    plt.axis('image')
    plt.axis([-3, 3, -3, 3])
    plt.title('r = ' + str(r))

rs = [-1, -0.1, 0, .1, 1]
for i in range(len(rs)):
    fig.add_subplot(1, len(rs), i + 1)
    r = rs[i]
    plot_phase_space()