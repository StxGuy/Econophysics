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


F = np.linspace(0,1,100)

for alfa in [1.5,2,3]:
    L = [1-(1-Fn)**(1-1.0/alfa) for Fn in F]
    pl.plot(F,L)
    
pl.plot([0,1],[0,1],'k:')    
pl.axis([0,1,0,1])
pl.grid(True)
pl.xlabel('F')
pl.ylabel('L(F)')
pl.title('Lorenz Curve')
pl.legend(['a=1.5','a=2','a=3'])
pl.savefig('../chapters/Chapter_2/figures/src/Lorenz.svg')
pl.show()
