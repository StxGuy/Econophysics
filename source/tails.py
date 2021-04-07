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
# Study distribution tails
#---------------------------------------

mu = 0
b = 1
std = np.sqrt(2)*b
a = 3
xo = 0.5*(a-1)*np.sqrt((a-2)/a)*std

x = np.linspace(1,14,1000)

Gaussian = [(1.0/(std*np.sqrt(2*np.pi)))*np.exp(-0.5*(ex-mu)**2/std) for ex in x]
Laplace = [(0.5/b)*np.exp(-abs(ex-mu)/b) for ex in x]
Pareto = [(a*xo**a)/(ex**(a+1)) for ex in x]

if False:
    pl.loglog(x,eg)
    pl.loglog(x,ed)
    pl.loglog(x,ep)
    pl.axis([1,100,1E-8,1])
else:
    pl.plot(x,Gaussian,':',color='#909090')
    pl.plot(x,Laplace,'--',color='#C0C0C0')
    pl.plot(x,Pareto,color='#101010')
    pl.axis([1,14,0,0.004])
    
pl.legend(['Gaussian','Laplace','Pareto'])    
pl.xlabel('x')
pl.ylabel('f(x)')
pl.title('Distributions')
#pl.savefig('../chapters/Chapter_2/figures/src/tails.svg')
pl.show()
