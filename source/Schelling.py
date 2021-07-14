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

import os

os.system('clear')

import numpy as np
import matplotlib.pyplot as pl


def move(t,frm,to):
    k = t[frm]
    t[frm] = 0
    t[to] = k
            
def destination(t):
    unoccupied = np.where(t == 0)
    l = len(unoccupied[0])
    p = np.random.randint(l)
    
    m = unoccupied[0][p]
    n = unoccupied[1][p]
    
    return (m,n)

def neighborhood(t,k):
    p = np.zeros(np.shape(t))
    
    # Von Neumann neighborhood
    p[:,:-1] = t[:,1:]
    p[:,1:] = p[:,1:] + t[:,:-1]
    p[:-1,:] = p[:-1,:] + t[1:,:]
    p[1:,:] = p[1:,:] + t[:-1,:]
    
    p = np.where(t != 0, p*t,0)
    p = np.where(p < -k, p, 0)
    
    return p
                
def createGrid(rho,N):
    return np.array([[np.random.choice([0,-1,1],p=[rho,(1-rho)/2,(1-rho)/2]) for i in range(N)] for j in range(N)])

def cluster(t,y,x,c):
    L = np.shape(t)[0]
    mass = 0
    
    candidates = [(y,x)]
    while(len(candidates)>0):
        y,x = candidates.pop()
        if (t[y,x] == c):
            if (y > 0):
                candidates.append((y-1,x))
            if (y < L-1):
                candidates.append((y+1,x))
            if (x > 0):
                candidates.append((y,x-1))
            if (x < L-1):
                candidates.append((y,x+1))
                                
            mass = mass + 1
            t[y,x] = 3
            
    return mass

def segregation(t):
    L = np.shape(t)[0]
    n = []
    
    for j in range(L):
        for i in range(L):
            mass = cluster(t,j,i,1)
            if (mass > 0):
                n = np.append(n,mass)
            mass = cluster(t,j,i,-1)
            if (mass > 0):
                n = np.append(n,mass)
                

    return 2*np.sum(n**2)/np.sum(t!=0)**2

def simul(rho):
    print(rho)
    nei_space = [1,2,3,4]
    seg = []

    for nei in nei_space:
        print(nei)
            
        grid = createGrid(rho,80)
        #pl.figure(1)
        #pl.imshow(grid,cmap='gray')
        #pl.savefig('../chapters/Chapter_8/figs/src/Schelling1.svg')

        for it in range(150000):
            nbr = neighborhood(grid,nei)
            frm = np.unravel_index(nbr.argmin(),nbr.shape)
            to = destination(grid)
            move(grid,frm,to)

        #pl.figure(2)
        #pl.imshow(grid,cmap='gray')
        #pl.savefig('../chapters/Chapter_8/figs/src/Schelling2.svg')
        #pl.colorbar()
        #print(segregation(grid))
        #pl.show()
        seg.append(segregation(grid))
        
    return seg

s1 = simul(0.01)
s2 = simul(0.05)
s3 = simul(0.10)
s4 = simul(0.15)
x = [1,2,3,4]

pl.plot(x,s1,'s-',color='gray')
pl.plot(x,s2,'o-',color='darkgray')
pl.plot(x,s3,'*-',color='silver')
pl.plot(x,s4,'^-',color='lightgray')
pl.axis([0.85,4.15,0,0.4])
pl.legend([0.01,0.05,0.10,0.15])
pl.savefig('../chapters/Chapter_8/figs/src/Schelling3.svg')
pl.show()
