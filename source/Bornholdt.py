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
import random as rd
import matplotlib.pyplot as pl
from math import isnan

def neig(i,j,N):
    z = []
    if (i > 0):
        z.append([i-1,j])
    if (i < N-1):
        z.append([i+1,j])
    if (j > 0):
        z.append([i,j-1])
    if (j < N-1):
        z.append([i,j+1])
        
    return np.array(z)

    

N = 32
J = 1.0
beta = 1.0/1.5
alpha = 4.0

S = np.array([rd.choices([1,-1],k=N) for i in range(N)])
C = np.array([rd.choices([1,-1],k=N) for i in range(N)])
Sn = np.zeros((N,N))
Cn = np.zeros((N,N))

r = []
cauda = []
M = 1
Steps = 100
for it in range(Steps):
    Ml = M
    M = np.average(S)
    for i in range(N):
        for j in range(N):
            sm = 0
            for x in neig(i,j,N):
                sm = sm + S[x[0],x[1]]
                
            h = J*sm - alpha*C[i,j]*M
            p = 1.0/(1+np.exp(-2*beta*h))
            
            if (rd.random() < p):
                Sn[i,j] = 1
            else:
                Sn[i,j] = -1
                
            if (alpha*S[i,j]*C[i,j]*sm < 0):
                Cn[i,j] = -C[i,j]
            else:
                Cn[i,j] = C[i,j]

    S = Sn
    C = Cn
    rt = np.log10(abs(M))-np.log10(abs(Ml))
    if (abs(rt) < 100):
        r = np.append(r,rt)
        if (rt > 0):
            cauda.append(rt)

mi = min(r)
ma = max(r)
#pl.figure(1)
#pl.plot(r)
#pl.axis([0,Steps,-0.1,0.1])
#pl.savefig('../chapters/Chapter_8/figs/src/Bornts.svg')


x = np.linspace(mi,ma,100)
y = []
for ex in x:
    y.append(1.0-float(sum(cauda<ex))/len(cauda))

#pl.figure(2)    
#pl.loglog(x,y,'.')
#pl.savefig('../chapters/Chapter_8/figs/src/Bornts.svg')
#pl.show()


pl.imshow(S,cmap='gray')
pl.show()
#pl.savefig('../chapters/Chapter_8/figs/src/Born1.svg')

#pl.plot(r)
#pl.axis([0,200,-0.04,0.04])
#pl.savefig('../chapters/Chapter_8/figs/src/Bornts.svg')


#pl.hist(r)
#pl.savefig('../chapters/Chapter_8/figs/src/Bornh.svg')


#pl.show()
