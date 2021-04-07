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

#---------------------------------------
# DESCRIPTION
#
# Marcenko-Pastur distribution
#---------------------------------------

n = 77
M = 100
eta = 1E-3

#----------------------- Theoretical curve ------------------
c = n/M

ea = (1+np.sqrt(c))**2
eb = (1-np.sqrt(c))**2

esp = np.linspace(eb,ea,100)
rsp = []

for e in esp:
    if e == 0:
        r = max(0,1-1.0/c)
    else:
        r = (float(c)/(2*np.pi*e))*np.sqrt((e-ea)*(eb-e))
    
    rsp.append(r)

#---------------------- Experimental curve ----------------    
DOS = []
for it in range(300):
    R = np.array([[np.random.normal(0,1) for cn in range(n)] for cm in range(M)])
    H = np.dot(R,np.transpose(R))
    N = len(H)
    H = np.dot(1.0/N,H)
    
    gsp = []
    for e in esp:
        G = np.linalg.inv((e+1j*eta)*np.eye(N)-H)
        r = -(1.0/(N*np.pi))*np.trace(G.imag)
        gsp.append(r)
    
    DOS.append(gsp)
        
DOS = np.average(DOS,axis=0)
    
pl.plot(esp,rsp,color='lightgray')
pl.plot(esp,DOS,'.',color='gray')
pl.axis([0,3.75,0,1.2])
pl.xlabel('Eigenvalue')
pl.ylabel('Density')
pl.show()
                 
