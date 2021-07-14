# -*- coding: utf-8 -*-
#!/usr/bin/env python

__author__ = """Prof. Carlo R. da Cunha, Ph.D. <creq@if.ufrgs.br>"""

import os

os.system('clear')
print('.-------------------------------.')
print('|                               |#')
print('| By.: Prof. Carlo R. da Cunha  |#')
print('|                               |#')
print('|                         2020  |#')
print('\'-------------------------------\'#')
print('  ################################')
print('')
print('Importing Libraries:')

import matplotlib.pyplot as pl
import numpy as np


def LV(xo,yo,p):
    alpha = p[0]
    beta = p[1]
    delta = p[2]
    gamma = p[3]
    
    h = 0.04

    x = xo
    y = yo
    xsp = []
    ysp = []
    for i in range(750):
        x = x/(1-h*(alpha-beta*y))
        y = y*(1+h*(delta*x-gamma))

        xsp.append(x)
        ysp.append(y)
        
    return xsp,ysp
    
def Pot(xo,yo,p):
    alpha = p[0]
    beta = p[1]
    delta = p[2]
    gamma = p[3]
    
    return alpha*np.log(yo) + gamma*np.log(xo) - beta*yo - delta*xo


#------------------ MAIN -----------------#
sigma = 0.5
lbd = 0.8
theta = 0.3
rho = 0.5
eta = 0.6

alpha = 1.0/sigma - lbd - theta
beta = 1.0/sigma
delta = rho
gamma = eta + lbd

p = [alpha,beta,delta,gamma]

#-- Fig. 1 --#
pl.figure(1)

xi,yi = 0.25,0.37
x,y = LV(xi,yi,p)
V1 = Pot(xi,yi,p)
pl.plot(x,y,'gray')

xi,yi = 0.35,0.27
x,y = LV(xi,yi,p)
V2 = Pot(xi,yi,p)
pl.plot(x,y,'lightgray')

xi,yi = 0.42,0.23
x,y = LV(xi,yi,p)
V3 = Pot(xi,yi,p)
pl.plot(x,y,'silver')
pl.legend(['V=-3.70','V=-3.36','V=-3.21'],loc='upper right')

pl.plot(gamma/delta,alpha/beta,'ko')

pl.xlabel('Employment rate - u')
pl.ylabel('Wage share - v')
pl.savefig('../chapters/Chapter_7/figs/src/LV1.svg')

#-- Fig. 2 --#
pl.figure(2)

x,y = LV(0.25,0.45,p)

pl.plot(x,color='gray')
pl.plot(y,color='silver')
pl.xlabel('Time')
pl.legend(['Employment rate - u','Wage share - v'],loc='upper left')
pl.axis([0,750,0,12])
pl.savefig('../chapters/Chapter_7/figs/src/LV2.svg')

pl.show()
