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

def cor(M):
    L = np.shape(M)[0]>>1
    
    F = np.fft.fft2(M)
    S = F*np.conj(F)/np.size(M)
    T = np.fft.ifft2(S).real
    
    y = np.log(T[L,1:L])
    x = range(len(y))
    
    
    return 1.0/abs(np.cov(x,y)[0][1]/np.var(x))   
    
    #return T[L,1:L]
  
def sandpile(L):
    grid = np.zeros((L,L))

    xo = L >> 1
    yo = L >> 1
    grid[yo,xo] = 1E5

    y = []
    it = 0
    #while(np.max(grid) >= 4):
    for it in range(85000):
        # Find unstable cells
        to_topple = (grid >= 4)
        
        # Toppling
        grid[to_topple] -= 4
        grid[1:,:][to_topple[:-1,:]] += 1
        grid[:-1,:][to_topple[1:,:]] += 1
        grid[:,1:][to_topple[:,:-1]] += 1
        grid[:,:-1][to_topple[:,1:]] += 1
        
        # Spillover
        grid[0,:] = 0
        grid[L-1,:] = 0
        grid[:,0] = 0
        grid[:,L-1] = 0
        
        if (not(it % 2000)):
            y.append(cor(grid))
        
        it += 1

    color_map = pl.cm.get_cmap('gray')
    reversed_color_map = color_map.reversed()    
    pl.imshow(grid,cmap=reversed_color_map)
    pl.colorbar()
    print(grid[yo+1,xo+1])
    
    pl.show()
        
    return y

if (False):
    z = []
    x = [30,40,50,60,70,80,90]
    for n in x:
        y = sandpile(n)
        z.append(np.average(y[-10:]))

    pl.loglog(x,z,'s',color='gray')
    pl.axis([20,100,100,1E4])
    #pl.savefig('../chapters/Chapter_6/figs/src/piledcis.svg')

    pl.show()



if (False):
    C = -2.2
    D = 2.2

    L = 30    
    y = sandpile(L)
    x = np.linspace(0,len(y)/L**D,len(y))
    z = [e*(L**C) for e in y]
    pl.loglog(x,z,'.',color='gray')

    L = 50
    y = sandpile(L)
    x = np.linspace(0,len(y)/L**D,len(y))
    z = [e*(L**C) for e in y]
    pl.loglog(x,z,'s',color='lightgray')

    L = 70
    y = sandpile(L)
    x = np.linspace(0,len(y)/L**D,len(y))
    z = [e*(L**C) for e in y]
    pl.loglog(x,z,'^',color='silver')

    L = 90
    y = sandpile(L)
    x = np.linspace(0,len(y)/L**D,len(y))
    z = [e*(L**C) for e in y]
    pl.loglog(x,z,'*',color='dimgrey')

    pl.legend([30,50,70,90])
    pl.axis([4E-4,8E-3,1E-4,1E1])

    #pl.axis([0,80,0,14000])
    #pl.savefig('../chapters/Chapter_6/figs/src/piledc.svg')
    pl.show()


sandpile(90)

if (False):
    color_map = pl.cm.get_cmap('gray')
    reversed_color_map = color_map.reversed()    
    pl.imshow(grid,cmap=reversed_color_map,interpolation='bilinear')
    pl.colorbar()
    #pl.savefig('../chapters/Chapter_6/figs/src/pile.svg')
    pl.show()

    
