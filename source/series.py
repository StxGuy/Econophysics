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

import matplotlib.pyplot as pl
import numpy as np

#---------------------------------------
# DESCRIPTION
#
# Time series
#---------------------------------------

if (False):
    s_space = [0,1,2,3,4,5,6,7,8,9,10]
    w_space = np.linspace(0,np.pi,100)

    phi1 = -0.75
    phi2 = -0.50
    phi3 = 0.50
    phi4 = 0.75

    rho1 = [phi1**s for s in s_space]
    rho2 = [phi2**s for s in s_space]
    rho3 = [phi3**s for s in s_space]
    rho4 = [phi4**s for s in s_space]

    S1 = [1.0/(1-2*phi1*np.cos(omega)+phi1**2) for omega in w_space]
    S2 = [1.0/(1-2*phi2*np.cos(omega)+phi2**2) for omega in w_space]
    S3 = [1.0/(1-2*phi3*np.cos(omega)+phi3**2) for omega in w_space]
    S4 = [1.0/(1-2*phi4*np.cos(omega)+phi4**2) for omega in w_space]

    fig = pl.figure(1)
    spec = fig.add_gridspec(wspace=0,ncols=2,nrows=1)

    ax1 = fig.add_subplot(spec[0,0])
    ax1.plot(s_space,[0 for n in s_space],':',color='lightgrey')
    ml,sl,bl = ax1.stem(s_space,rho4,markerfmt='s',linefmt='lightgrey',basefmt='none',use_line_collection=True,label=r'$\phi=0.75$')
    pl.setp(ml,'color','lightgrey')
    ml,sl,bl = ax1.stem(s_space,rho2,markerfmt='o',linefmt='grey',basefmt='none',use_line_collection=True,label=r'$\phi=-0.5$')
    pl.setp(ml,'color','grey')
    ax1.set_xlabel('s')
    ax1.set_ylabel('Autocorrelation')
    ax1.legend()

    ax2 = fig.add_subplot(spec[0,1])
    w_space = np.linspace(0,1,100)
    ax2.plot(w_space,S4,color='k',label=r'$\phi=0.75$')
    ax2.plot(w_space,S3,color='grey',label=r'$\phi=0.50$')
    ax2.plot(w_space,S2,color='darkgrey',label=r'$\phi=-0.50$')
    ax2.plot(w_space,S1,color='lightgrey',label=r'$\phi=-0.75$')
    ax2.set_xlabel(r'$\omega/\pi$')
    ax2.set_ylabel('Spectral density')
    ax2.yaxis.set_label_position('right')
    ax2.set_xlim([0,1])
    ax2.set_ylim([0,17])
    ax2.set_xticks(ax2.get_xticks()[1:])
    ax2.yaxis.tick_right()
    ax2.legend()

else:
    theta1 = 0.75
    theta2 = 0.50
    theta3 = -0.50
    theta4 = -0.75
    w_space = np.linspace(0,np.pi,100)

    S1 = [1 + theta1**2 + 2*theta1*np.cos(w) for w in w_space]
    S2 = [1 + theta2**2 + 2*theta2*np.cos(w) for w in w_space]
    S3 = [1 + theta3**2 + 2*theta3*np.cos(w) for w in w_space]
    S4 = [1 + theta4**2 + 2*theta4*np.cos(w) for w in w_space]    
    
    fig = pl.figure(2)

    w_space = np.linspace(0,1,100)
    pl.plot(w_space,S1,color='lightgrey',label=r'$\theta=0.75$')
    pl.plot(w_space,S2,color='darkgrey',label=r'$\theta=0.50$')
    pl.plot(w_space,S3,color='grey',label=r'$\theta=-0.50$')
    pl.plot(w_space,S4,color='k',label=r'$\theta=-0.75$')
    pl.legend()
    pl.axis([0,1,0,3.5])
    pl.xlabel(r'$\omega/\pi$')
    pl.ylabel('Spectral density')
    

pl.show()

    
