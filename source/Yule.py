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

#---------------------------------------
# DESCRIPTION
# Yule-Furry process
#---------------------------------------

n_sp = range(3,50)
l = 0.08
m = 2

def binom(n,k):
	if k == 0:
		r = 1
	else:
		r = (n/k)*binom(n-1,k-1)
	return round(r)
	

t = 10
x = [binom(n-1,m-1)*np.exp(-l*t)*(1-np.exp(-l*t))**(n-m) for n in n_sp]
pl.plot(n_sp,x,'o-',color='#444444')
	
t = 20
x = [binom(n-1,m-1)*np.exp(-l*t)*(1-np.exp(-l*t))**(n-m) for n in n_sp]
pl.plot(n_sp,x,'^-',color='#888888')

t = 30
x = [binom(n-1,m-1)*np.exp(-l*t)*(1-np.exp(-l*t))**(n-m) for n in n_sp]
pl.plot(n_sp,x,'s-',color='#bbbbbb')
	

pl.legend(['t=5','t=15','t=25'])
pl.xlabel('n')
pl.ylabel('X$_n$')
pl.axis([2.7,30,-0.03,0.6])
pl.title('Yule-Furry with $\lambda=0.08$ and $m=2$')
pl.show()
