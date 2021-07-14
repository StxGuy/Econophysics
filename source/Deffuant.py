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

def simul(b):
    NA = 50
    NI = 40000
    mu = 0.35

    x = np.zeros((NA,NI))
    x[:,0] = [np.random.uniform() for i in range(NA)]

    for t in range(NI-1):
        i = np.random.randint(NA)
        j = np.random.randint(NA)
        
        x[:,t+1] = x[:,t]
        if abs(x[i,t]-x[j,t]) < b:
            x[i,t+1] = x[i,t] - mu*(x[i,t]-x[j,t])
            x[j,t+1] = x[j,t] - mu*(x[j,t]-x[i,t])
            
            
    #for i in range(NA):
    #    c = 0.5*float(i)/NA
    #    pl.plot(x[i,:],'-',color=(c,c,c))
    #pl.axis([0,NI-1,0,1])            

    y = []
    for e in x[:,NI-1]:
        y.append(round(e,2))
                
    N = len(Counter(y).keys())
    #print(N)
            
            
    return(N)
        
if (False):
    #for i in range(NA):
    #    c = 0.5*float(i)/NA
    #    pl.plot(x[i,:],'-',color=(c,c,c))
    #pl.axis([0,NI-1,0,1])
    #pl.savefig('../chapters/Chapter_8/figs/src/Deffuant.svg')
    simul(0.10)
    pl.show()
else:
    bl = np.linspace(0.01,0.20,20)
    y = [simul(b) for b in bl]

    A,B = plfit(bl,y)
    print(A,B)
    z = [A*x**B for x in bl]

    pl.loglog(bl*100,z,color='lightgray')
    pl.loglog(bl*100,y,'.',color='gray')
    pl.axis([0.8,30,1,100])
    #pl.savefig('../chapters/Chapter_8/figs/src/Deffuant2.svg')
    pl.show()
    
