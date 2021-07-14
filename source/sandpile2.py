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

# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7

__author__ = """Prof. Carlo R. da Cunha, Ph.D. <creq@if.ufrgs.br>"""

import os

os.system('clear')


import numpy as np
import matplotlib.pyplot as pl


#############################################
# COLOCA GRAO DE AREIA EM UMA POSICAO       #
#############################################
def place(array,x,y,L):
	ac = 0
	if (x >= 0 and x < L) and (y >= 0 and y < L):
		array[x][y] = array[x][y] + 1
		
		# Toppling
		if array[x][y] >= 4:
			ac = ac + 1
			array[x][y] = array[x][y] - 4
			array,t1 = place(array, x+1, y, L)
			array,t2 = place(array, x-1, y, L)
			array,t3 = place(array, x, y+1, L)
			array,t4 = place(array, x, y-1, L)
			ac = ac + t1 + t2 + t3 + t4 		
	return array, ac

#############################################
# INTERACAO                                 #
#############################################
def dist(L):
	sand = [[0 for n in range(L)] for m in range(L)]
	massa = []
	tops = [0 for n in range(50000)]
	
	N = 500*L+100
	for it in range(N):
		x = np.random.binomial(L,0.5)
		y = np.random.binomial(L,0.5)
		sand,t = place(sand, x, y, L)
		
		massa = np.append(massa, np.mean(sand))
		tops[t] = tops[t] + 1

	return massa, tops

#############################################
# MAIN                                      #
#############################################

N = 80
a,t = dist(N)

x = []
y = []
for n in range(len(t)):
#	if t[n] > 0 and n > 0:
#		y = np.append(y, np.log(t[n]))
#		x = np.append(x, np.log(n))	
    x = np.append(x,n)
    y = np.append(y,t[n])


#a = np.cov(x,y)[0][1]/np.var(x)
#print(a)
pl.loglog(x,y,'.',color='gray')

pl.xlabel('Size of avalance')
pl.ylabel('Number of avalanches')
pl.axis([1E-1,1E3,1E1,1E4])
pl.savefig('../chapters/Chapter_6/figs/src/pilehist.svg')
pl.show()
quit()


		
