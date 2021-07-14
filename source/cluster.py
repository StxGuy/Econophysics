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

def gclust(A):
    N = np.shape(A)[0]

    num = np.trace(np.linalg.matrix_power(A,3))
    
    k = [0 for j in range(N)]
    for i in range(N):
        for j in range(N):
            k[i] = k[i] + A[i,j]
        
    den = 0
    for i in range(N):
        den = den + k[i]*(k[i]-1)
        
        
    print(num)
    print(den)
    return num/den
    

A = np.array([[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]])
A = np.array([[0,1,1,4],[1,0,0,0],[1,0,0,1],[1,0,1,0]])
A = np.array([[0,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]])
A = np.array([[0,1,0,1],[1,0,1,1],[0,1,0,1],[1,1,1,0]])
print(gclust(A))
