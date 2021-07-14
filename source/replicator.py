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

def fun(p,V,C):
    return 0.5*p*(p-1)*(p*C-V)


def RK(po,V,C):
    h = 0.1
    p = po
    
    x = []
    for i in range(1000):
        k1 = fun(p,V,C)
        k2 = fun(p + 0.5*h*k1,V,C)
        k3 = fun(p + 0.5*h*k2,V,C)
        k4 = fun(p + h*k3,V,C)

        p = p + (h/6)*(k1+2*k2+2*k3+k4)
        x.append(p)

    return x

pl.semilogx(RK(0.001,2,1),color='gray')
pl.semilogx(RK(0.001,1,1.5),color='lightgray')
pl.semilogx(RK(0.001,1,2),color='silver')
pl.legend(['V=2,C=1','V=1,C=1.5','V=1,C=2'])
pl.axis([10,1000,0,1.2])
pl.xlabel('Time')
pl.ylabel('p')
pl.savefig('../chapters/Chapter_7/figs/src/replic.svg')
pl.show()
