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
import pandas as pd

from datetime import datetime
from scipy.stats import norm


# Get historical data
s = pdr.get_data_yahoo(symbols="^GSPC",start=datetime(2019,10,4),end=datetime(2020,5,27))
idx = pd.date_range('10-04-2019','05-27-2020')
s.index = pd.DatetimeIndex(s.index)
s = s.reindex(idx)
s = s.interpolate()

dt = pd.read_csv("coro.csv",parse_dates=['Dia'])


if False:
    fig,ax1 = pl.subplots()
    ax2 = ax1.twinx()

    ax1.plot(s['Adj Close'],color='gray')
    ax2.plot(d['Dia'],d['coronavirus'],color='lightgray')

    ax1.tick_params(axis='x',rotation=45)
    ax1.set_ylabel('Closing Values',color='gray')
    ax1.set_xlabel('Date')
    ax1.set_xlim(datetime(2019,10,4),datetime(2020,5,27))

    ax2.set_ylabel('Trend',color='lightgray')
    ax2.set_xlim(datetime(2019,10,4),datetime(2020,5,27))
    
    pl.show()

else:
    ts = s['Adj Close']
    tc = dt['coronavirus']

    m = np.mean(ts)
    s = np.std(ts)
    ts = [(e-m)/s for e in ts]
    
    m = np.mean(tc)
    s = np.std(tc)
    tc = [(e-m)/s for e in tc]

    m = [[0 for a in range(5)] for b in range(5)]
    p = [[0 for a in range(5)] for b in range(5)]
    n = [0 for a in range(5)]
    c = [0,0,1,1,0,3]
    d = [0,1,0,1,-1,0]
    
    #i = [0,0,0,0,1]
    #j = [0,1,2,3,0]
    #i = [0,0,0,1,1]
    #j = [0,1,2,0,1]
    i = [0,0,1,1,0]
    j = [0,1,0,1,2]
    ac = 0
    for X,Y in zip(ts,tc):
        for a in range(5):
            n[a] = n[a] + (X**(i[a]+3))*(Y**j[a])
            
            for b in range(5):
                m[a][b] = m[a][b] + (X**(i[a]+c[b]))*(Y**(j[a]+d[b]))
            
        ac = ac + 1

    # Compute averages
    for a in range(5):
        p[a] = [1,1,-2,-2,0.5*j[a]]
        n[a] = n[a]/ac
        
        for b in range(5):
            m[a][b] = m[a][b]/ac
    
         
    M = [[m[a][b]*p[a][b] for b in range(5)] for a in range(5)]
    b = [[-4*n[a]] for a in range(5)]
    
    coef = np.linalg.solve(M,b)
    
    print("Coefficients:")
    print(coef)
    ao = coef[0]
    a1 = coef[1]
    bo = coef[2]
    b1 = coef[3]
    sg = coef[4]

    X = ts[0]
    xsp = []
    dt = 1E-3
    for Y in tc:
        a = ao + a1*Y
        b = bo + b1*Y
        X = X + (4*X**3 - 2*b*X + a)*dt + norm.rvs(scale=np.sqrt(sg)*dt)
        xsp.append(X)
    
    pl.plot(idx,ts,color='Gray')
    pl.plot(idx,xsp,color='Silver')
    
    pl.legend(['Closing Value','Fitting'])
    pl.xlabel('Time')
    pl.ylabel('Normalized Values')
    
    ax = pl.gca()
    ax.tick_params(axis='x',rotation=45)
    ax.set_xlim(datetime(2019,10,4),datetime(2020,5,27))
    
    #pl.axis([0,237,-3.5,2])
    pl.savefig('../chapters/Chapter_6/figs/src/catdyn.svg')
    pl.show()
