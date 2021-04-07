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
from scipy.stats import norm

#---------------------------------------
# DESCRIPTION
#
# Simulate Black-Scholes
#---------------------------------------

r = 0.094/100       # Risk-free rate: US 3 month treasure bill
k = 125.0           # Strike price: IBM on NYSE
sigma = 0.025       # Volatility: IBM from 02/10/2019-02/10/2020
sigma2 = sigma**2
tau = 0.1

# CDF Function
def phi(x):
    return norm.cdf(x)

# Body
S_space = np.linspace(120,130,100)
cor_space = ['#444444','#888888', '#BBBBBB']
tau_space = [0.01,0.1,1]

for tau,cor in zip(tau_space,cor_space):
    price = []
    for S in S_space:
        mu = np.log(S) + (r-0.5*sigma2)*tau
        d1 = (mu-np.log(k) + sigma2*tau)/(sigma*np.sqrt(tau))
        d2 = d1 - sigma*np.sqrt(tau)
        
        c = S*phi(d1)-k*np.exp(-r*tau)*phi(d2)
        price.append(c)
        
    pl.plot(S_space,price,color=cor)

# Plotting
pl.legend([r'$\tau$=0.01',r'$\tau$=0.1',r'$\tau$=1'])
pl.axis([120,130,0,5])
pl.xlabel('Price of underlying asset')
pl.ylabel('Option payoff')
pl.show()
