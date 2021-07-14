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

import numpy as np
import matplotlib.pyplot as pl
from collections import Counter


def plfit(xsp,ysp):
    N = len(xsp)
    ac1 = 0.0
    ac2 = 0.0
    ac3 = 0.0
    ac4 = 0.0
    for xi,yi in zip(bl,ysp):
        ac1 = ac1 + np.log(xi)*np.log(yi)
        ac2 = ac2 + np.log(xi)
        ac3 = ac3 + np.log(yi)
        ac4 = ac4 + np.log(xi)**2
        
    b = (N*ac1 - ac2*ac3)/(N*ac4 - ac2**2)
    a = (ac3 - b*ac2)/N
    
    return np.exp(a),b


def neighborhood(S,el,t):
    ac = 0
    z = 0.0
    for y in S:
        if abs(y-el) <= t:
            z = z + y
            ac = ac + 1
            
    return z/ac

def simul(bl):
    NA = 50
    NI = 10

    x = np.zeros((NA,NI))
    x[:,0] = [np.random.uniform() for i in range(NA)]


    for t in range(NI-1):
        for i in range(NA):
            x[i,t+1] = neighborhood(x[:,t],x[i,t],bl)


    return(len(Counter(x[:,NI-1]).keys()))

bl = np.linspace(0.01,0.20,20)
y = [simul(b) for b in bl]

A,B = plfit(bl,y)
print(A,B)
z = [A*x**B for x in bl]

pl.loglog(bl*100,z,color='lightgray')
pl.loglog(bl*100,y,'.',color='gray')
pl.axis([0.8,30,1,100])
#pl.savefig('../chapters/Chapter_8/figs/src/HK2.svg')
pl.show()

#for i in range(NA):
#    c = 0.5*float(i)/NA
#    pl.plot(x[i,:],'.-',color=(c,c,c))
#pl.axis([0,NI-1,0,1])
#pl.savefig('../chapters/Chapter_8/figs/src/HK1.svg')
#pl.show()
