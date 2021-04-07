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
# Wigner's surmise
#---------------------------------------

s_space = np.linspace(0,3,100)
GOE = [0.5*np.pi*s*np.exp(-0.25*np.pi*s**2) for s in s_space]
GUE = [(32.0/(np.pi**2))*(s**2)*np.exp(-(4*s**2)/np.pi) for s in s_space]
GSE = [(2**18/(3**6*np.pi**3))*(s**4)*np.exp(-(64*s**2)/(9*np.pi)) for s in s_space]
Poi = [np.exp(-s) for s in s_space]

pl.plot(s_space,GOE,color='dimgray')
pl.plot(s_space,GUE,color='gray')
pl.plot(s_space,GSE,color='darkgray')
pl.plot(s_space,Poi,':',color='silver')
pl.xlabel('Spacing')
pl.ylabel('Distribution')
pl.axis([0,3,0,1.3])
pl.savefig('../chapters/Chapter_5/figs/src/surmise.svg')
pl.show()
