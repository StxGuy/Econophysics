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
# Security market line
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
ibm = pdr.get_data_yahoo(symbols='IBM',start=datetime(2013,1,1),end=datetime(2014,1,1))
amd = pdr.get_data_yahoo(symbols='AMD',start=datetime(2013,1,1),end=datetime(2014,1,1)) 
itl = pdr.get_data_yahoo(symbols='INTC',start=datetime(2013,1,1),end=datetime(2014,1,1)) 
apl = pdr.get_data_yahoo(symbols='AAPL',start=datetime(2013,1,1),end=datetime(2014,1,1))
nvd = pdr.get_data_yahoo(symbols='NVDA',start=datetime(2013,1,1),end=datetime(2014,1,1)) 
ndxt = pdr.get_data_yahoo(symbols='^NDXT',start=datetime(2013,1,1),end=datetime(2014,1,1)) 


# Get Close Prices
pibm = ibm['Adj Close']
pamd = amd['Adj Close']
pitl = itl['Adj Close']
papl = apl['Adj Close']
pnvd = nvd['Adj Close']
pndxt = ndxt['Adj Close']


# Get Returns
ribm = ret(pibm)
ramd = ret(pamd)
ritl = ret(pitl)
rapl = ret(papl)
rnvd = ret(pnvd)
rndxt = ret(pndxt)

# Expected returns
Ribm = np.average(ribm)
Ramd = np.average(ramd)
Ritl = np.average(ritl)
Rapl = np.average(rapl)
Rnvd = np.average(rnvd)
Rndxt = np.average(rndxt)


# Betas
bibm = np.cov(ribm,rndxt)[0][1]/np.var(ribm)
bamd = np.cov(ramd,rndxt)[0][1]/np.var(ramd)
bitl = np.cov(ritl,rndxt)[0][1]/np.var(ritl)
bapl = np.cov(rapl,rndxt)[0][1]/np.var(rapl)
bnvd = np.cov(rnvd,rndxt)[0][1]/np.var(rnvd)


pl.plot(bibm,100*Ribm,'o')
pl.plot(bamd,100*Ramd,'+')
pl.plot(bitl,100*Ritl,'*')
pl.plot(bapl,100*Rapl,'s')
pl.plot(bnvd,100*Rnvd,'^')

ro = 0.01/100
b_space = np.linspace(0,1.2,100)
R = [100*(ro + b*(Rndxt-ro)) for b in b_space]
pl.plot(b_space,R)
pl.xlabel('Systematic risk')
pl.ylabel('Expected return')
pl.legend(['IBM','AMD','INTEL','APPLE','NVidia'])
pl.axis([0,1.2,-0.05,0.2])

pl.show()

