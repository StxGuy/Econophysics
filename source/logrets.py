# -*- coding: utf-8 -*-
#!/usr/bin/env python

__author__ = """Prof. Carlo R. da Cunha, Ph.D. <creq@if.ufrgs.br>"""

import os

os.system('clear')
print('.-------------------------------.')
print('|                               |#')
print('| By.: Prof. Carlo R. da Cunha  |#')
print('|                               |#')
print('|                         2021  |#')
print('\'-------------------------------\'#')
print('  ################################')
print('')
print('Importing Libraries:')

import numpy as np
import matplotlib.pyplot as pl
import pandas_datareader as pdr

from datetime import datetime

#---------------------------------------
# DESCRIPTION
#
# Compute log-returns
#---------------------------------------

# Log-returns
def ret(x):
	N = len(x)
	
	y = []
	for i in range(N-1):
		r = np.log(x[i+1])-np.log(x[i])
		y.append(r)
		
	return y

# Covariance        
def cv(x,y):
	return np.cov(x,y)[0][1]	

# a.b.c
def tri(a,b,c):
	return np.dot(a,np.dot(b,c))

# Get historical data
gme = pdr.get_data_yahoo(symbols='GME',start=datetime(2013,10,1),end=datetime(2021,1,28))

# Get Close Prices
price = gme['Adj Close']

pl.semilogy(price)
pl.show()
