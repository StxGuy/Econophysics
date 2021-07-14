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
import random as rd
import matplotlib.pyplot as pl


# binary to integer
def val(x):
    r = 0
    for i in range(len(x)):
        if (x[i] == 1):
            r = r + (1 << i)
                
    return r

# Push value into array
def push(v,x):
    for i in range(len(v)-2,-1,-1):
        v[i+1]=v[i]
    v[0] = x
    
    return v

# Auxiliary odd function for the payoff
def g(x,N):
    return x/N

# Class for agents
class agent:
    def __init__(self,m,s):
        # Memory
        self.m = m
        # Strategies
        self.s = s
        self.r = [rd.choices([-1,1],k=2**m) for a in range(s)]
        # Points
        self.p = [rd.random() for a in range(s)]

    def update_points(self,pos,W,A,N):
        for strategy in range(self.s):
            r_a = self.r[strategy]
            self.p[strategy] = self.p[strategy] - (r_a[pos]*A)/(2**self.m)
           
        
    def a(self,pos):
        winning_strategy = np.argmax(self.p)
        r_beta = self.r[winning_strategy]
        return r_beta[pos]


# Minority Game
def game(N,numStrategies,memory):
    player = [agent(memory,numStrategies) for i in range(N)]
    bits = rd.choices([-1,1],k=memory)

    # Loop over interactions
    At = []
    S = [0 for i in range(2**memory)]
    P = [0 for i in range(2**memory)]
    for it in range(500):
        # Calculate attendance
        mu = val(bits)
        A_space = [player[i].a(mu) for i in range(N)]
        A = np.sum(A_space)
        At.append(A)

        # Winning group
        W = -np.sign(A)
        bits = push(bits,W)
        
        # Update virtual score
        for i in range(N):
            player[i].update_points(mu,W,A,N)
                
        # Calculate information
        for nu in range(2**memory):
            if (mu == nu):
                S[nu] = S[nu] + A
                P[nu] = P[nu] + 1
    
    # Calculate information
    H = 0
    for n in range(2**memory):
        if (P[n] > 0):
            H = H + (S[n]/P[n])**2

    
    # Calculate variance
    s = np.var(At)
    
    return s,H/2**memory

#======================================================#
#                        MAIN                          #
#======================================================#

if False:
    a,b,x1 = game(301,2,2)
    a,b,x2 = game(301,2,7)
    
    pl.plot(x1,color='gray')
    pl.plot([x+250 for x in x2],color='silver')
    pl.axis([0,200,-200,325])
    pl.xlabel('t')
    pl.ylabel('A(t)')
    pl.savefig('../chapters/Chapter_6/figs/src/minor_inset.svg')
    pl.show()
    

if True:
    # Average Av samples
    Av = 20

    # Data collapse
    for N,t,c in zip([31,51,71],['.','s','*'],['gray','lightgray','silver']):
        a_space = []
        s_space = []
        h_space = []
        for m in range(1,12):
            s = 0
            H = 0
            for av in range(Av):
                si,Hi = game(N,2,m)
                s = s + si
                H = H + Hi
            s = s/Av
            H = H/Av
            s_space.append(s/N)
            a_space.append((2**m)/N)
            h_space.append(H/N)

        pl.semilogx(a_space,h_space,t,color=c)
        

        
    pl.xlabel(r'$\alpha=2^m/N$')
    #pl.ylabel(r'$\sigma^2/N$')
    pl.ylabel('H/N')
    #pl.axis([1E-2,1E2,1E-1,1E2])
    pl.axis([1E-2,1E2,0,0.6])
    pl.legend([31,51,71])
    #pl.grid(True)
    pl.savefig('../chapters/Chapter_7/figs/src/minorH.svg')
    pl.show()
