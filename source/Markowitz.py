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
import pandas_datareader as pdr

from datetime import datetime

#---------------------------------------
# DESCRIPTION
#
# Markowitz portfolio theory
#---------------------------------------

def ret(x):
	N = len(x)
	
	y = []
	for i in range(N-1):
		r = np.log(x[i+1])-np.log(x[i])
		y.append(r)
		
	return y
        
def cv(x,y):
	return np.cov(x,y)[0][1]	

def tri(a,b,c):
	return np.dot(a,np.dot(b,c))

# Get historical data
ibm = pdr.get_data_yahoo(symbols='IBM',start=datetime(2011,1,1),end=datetime(2012,1,1))
amd = pdr.get_data_yahoo(symbols='AMD',start=datetime(2011,1,1),end=datetime(2012,1,1)) 
itl = pdr.get_data_yahoo(symbols='INTC',start=datetime(2011,1,1),end=datetime(2012,1,1)) 

# Get Close Prices
pibm = ibm['Adj Close']
pamd = amd['Adj Close']
pitl = itl['Adj Close']

# Get Returns
ribm = ret(pibm)
ramd = ret(pamd)
ritl = ret(pitl)

a = np.array([[np.average(ribm)],[np.average(ramd)],[np.average(ritl)]])
aT = np.transpose(a)

# Covariance Matrix
cii = cv(ribm,ribm)
caa = cv(ramd,ramd)
ctt = cv(ritl,ritl)

S = np.array([[cii,           cv(ribm,ramd), cv(ribm,ritl)],
	      [cv(ramd,ribm), caa,           cv(ramd,ritl)],
	      [cv(ritl,ribm), cv(ritl,ramd), ctt]])
Si = np.linalg.inv(S)	

# M Matrix
e = np.array([[1.0] for i in range(3)])
eT = np.transpose(e)

M = np.array([[ tri(eT,Si,e)[0][0], tri(aT,Si,e)[0][0]],
              [ tri(eT,Si,a)[0][0], tri(aT,Si,a)[0][0]]])
Mi = np.linalg.inv(M)


# Bullet
a_space = np.linspace(-0.002,0.005,100)
s_space = []
for ao in a_space:
	m = np.array([[1],[ao]])
	mT = np.transpose(m)

	s = tri(mT,Mi,m)[0][0]
	s_space.append(s)

# Plot
s_space = [np.sqrt(s)*100 for s in s_space]
a_space = [a*100 for a in a_space]

pl.plot(s_space,a_space)

pl.plot(100*np.sqrt(cii),a[0]*100,'o')
pl.plot(100*np.sqrt(caa),a[1]*100,'*')
pl.plot(100*np.sqrt(ctt),a[2]*100,'+')

pl.axis([1.2,3.7,-0.2,0.5])
pl.xlabel('Standard Deviation [%]')
pl.ylabel('Expected Return [%]')
pl.show()
	
