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

N = 100

# Set 1
eps1 = 0.005
delta1 = 0.01

# Set 2
eps2 = 0.01
delta2 = 0.02

# Set 3
eps3 = 0.15
delta3 = 0.3

eps = eps3
delta = delta3


k = N/2

x = []
for it in range(500000):
    p1 = (1-float(k)/N)*(eps+(1-delta)*float(k)/(N-1))
    p2 = (float(k)/N)*(eps+(1-delta)*(N-k)/(N-1))

    r = np.random.rand()

    if (r <= p1):
        k = k + 1
    if (r > p1 and r <= p1+p2):
        k = k - 1
        
    x.append(k)
    
#pl.plot(x,color='gray')
#pl.axis([0,500000,0,100])
pl.hist(x)
pl.savefig('../chapters/Chapter_8/figs/src/Kirmanh3.svg')
pl.show()
