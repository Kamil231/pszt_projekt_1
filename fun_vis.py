#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 00:40:40 2019

@author: kamil
"""

import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

from matplotlib import cm

def fun_vis():
    #f = lambda x, y: x**2 + y**2 + x*y - 500 
    #f = lambda x, y: x**3+y**3
    #f(x1, x2) = x21(4 − 2.1x21+ x41/3) + x1x2+ x22(−4 + 4x22)
    
    
    
    #f = lambda x,y: (x**2)*(4-2.1*(x**2)+(x**4)/3)+ x*y + (y**2)*(-4 + 4*(y**2))
    
    f = lambda x,y: x**5-25*x**3+y**5-25*y**3+400+30*(x**2)*y
    
    fig = plt.figure(figsize=(12,6))
    
    ax = fig.add_subplot(1,2,1,projection='3d')
    
    xvalues = np.linspace(-3,2,100)
    yvalues = np.linspace(-4.2,5,100)
    '''xvalues = np.linspace(-2.5,2.5,100)
    yvalues = np.linspace(-1.5,1.5,100)'''
    
    xgrid, ygrid = np.meshgrid(xvalues, yvalues)
    
    zvalues = f(xgrid, ygrid)
    
    surf = ax.plot_surface(xgrid, ygrid, zvalues,rstride=5, cstride=5,linewidth=0, cmap=cm.plasma)
    
    ax = fig.add_subplot(1,2,2)
    
    plt.contourf(xgrid, ygrid, zvalues, 30, cmap=cm.plasma)
    
    fig.colorbar(surf, aspect=18)
    
    plt.tight_layout()



