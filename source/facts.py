# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7

__author__ = """Prof. Carlo R. da Cunha, Ph.D. <creq@if.ufrgs.br>"""

import os

os.system('clear')
print ('.-------------------------------.')
print ('| API                           |#')
print ('| ---                           |#')
print ('|                               |#')
print ('| By.: Prof. Carlo R. da Cunha  |#')
print ('|                               |#')
print ('|                    July/2019  |#')
print ('\'-------------------------------\'#')
print ('  ################################')
print ('')
print ('Importing Libraries:')

from time import strptime, mktime
import datetime
import requests
import numpy as np
from datetime import date
import matplotlib.pyplot as pl

from scipy.optimize import curve_fit as cf
from scipy.stats import t
from scipy.stats import kurtosis as kurt
from random import choice

#---------------------------------------
# DESCRIPTION
#
# Snippet for studying stylized facts
#---------------------------------------

print ('Simulating...')
print ('')


def Gauss(x,Go,mu,sigma):
    return Go*np.exp(-0.5*((x-mu)/sigma)**2)

		
################################################
## CLASSE: Wallet                              #
#----------------------------------------------#
################################################
class market:
	
    def __init__(self):
        self.price = []
        self.nret = []
        self.lret = []
			
        if os.path.isfile('data.dat'):
            fp = open('data.dat','r')
			
            for line in fp:
                row = line.split()
                close = float(row[0])
                self.price.append(close)
				
            fp.close()
        else:			
            jetzt = datetime.datetime.now()
            jetzt = jetzt-datetime.timedelta(days=5)
            dk = datetime.timedelta(minutes=1000)
            d1 = datetime.timedelta(minutes=1)
            
            now = jetzt
            fp = open('data.dat','w')
            for n in range(10):
                to = now+dk
                fr = now
                epoch_fr = fr.strftime('%s')
                epoch_to = to.strftime('%s')
                now = to+d1
                
                url = "https://api.hitbtc.com/api/2/public/candles/BTCUSD?period=M1&limit=1000&from="+epoch_fr+"&till="+epoch_to
                r = requests.get(url)
                data = r.json()	
			                
                self.price = []
                for x in data:
                    close = float(x['close'])
                    tm = x['timestamp']
                    self.price.append(close)
                    fp.write(str(close)+' '+str(tm)+'\n')
                    
            fp.close()
            		
		# Calculate log-returns
        self.N = len(self.price)
        self.lret = []
        ac1 = 0
        ac2 = 0
        for n in range(self.N-1):
            lr = np.log(self.price[n+1]) - np.log(self.price[n])
            self.lret.append(lr)
            ac1 = ac1 + lr
            ac2 = ac2 + lr**2
			
        r1 = float(ac1)/(self.N-1)
        r2 = float(ac2)/(self.N-1)
			
		# Calcula normalized returns
        self.nret = []
        for n in range(self.N-1):
            self.nret.append((self.lret[n]-r1)/np.sqrt(r2-r1**2))
			
    def plot(self,num):
        #pl.plot(self.price)
        #pl.plot(self.nret)
        
        ma = max(self.nret)
        mi = min(self.nret)
        
        CDF = []
        x = []
        N = 200
        for n in range(N):
            m = mi + (ma-mi)*n/N
            CDF.append(1-np.average(self.nret > m))
            x.append(m)

        PDF = np.diff(CDF)
        
        # Gaussian fit
        popt,pcov = cf(Gauss,x[0:-1],PDF)
        
        # t-student fit
        param = t.fit(self.nret)
        ts_fit = t.pdf(x,loc=param[1],scale=param[2],df=param[0])
        s = np.sum(ts_fit)
        ts_fit = [ts/s for ts in ts_fit]
        
        if num == 1:
            fig1 = pl.figure(1)
            spec = fig1.add_gridspec(hspace=0,ncols=1,nrows=2)
            ax1 = fig1.add_subplot(spec[0,0])
            ax2 = fig1.add_subplot(spec[1,0])
            ax1.plot(self.price)
            ax1.set_ylabel('Price')
            ax1.set_xlim([0,7174])
            ax2.plot(self.nret)
            ax2.set_xlabel('Minutes')
            ax2.set_ylabel('Norm. Ret.')
            ax2.set_xlim([0,7174])
                    
        if num == 2:
            pl.figure(1)
            pl.semilogy(x[0:-1],PDF,'.',color='darkgrey')
            pl.semilogy(x,Gauss(x,*popt),':')
            pl.semilogy(x,ts_fit)
            pl.axis([-7.5,7.5,1E-4,3E-1])
            pl.xlabel('Normalized return')
            pl.ylabel('Distribution')
                    
        if num == 3:
            pl.figure(1)
            N = len(self.nret)
            s = [w*d for w,d in zip(np.hanning(N),self.nret)]
            N = int(pow(2,np.ceil(np.log(N)/np.log(2))))
            N2 = int(float(N)/2)            
            F = np.fft.fft(s,N)
            S = [f*np.conj(f)/N for f in F]
            z = np.fft.ifft(S).real
            C = z[0:N2]
            C = [c/C[0] for c in C]
            pl.semilogx(C,'*',color='darkgrey')
            s = [w*d*d for w,d in zip(np.hanning(N),self.nret)]
            F = np.fft.fft(s,N)
            S = [f*np.conj(f)/N for f in F]
            z = np.fft.ifft(S).real
            C = z[0:N2]
            C = [c/C[0] for c in C]
            pl.semilogx(C,'.',color='grey')
            pl.axis([0.72,3400,-0.1,0.5])
            pl.grid(True,linestyle=':')
            pl.xlabel('Time [min]')
            pl.ylabel('Autocorrelation')
            pl.legend([r'$r$',r'$r^2$'])
                        
        if num == 4:
            ku = []
            L = len(self.price)
            x = range(1,300,1)
            for lag in x:
                data = self.price[0:L:lag]
                ret = []
                for n in range(len(data)-1):
                    ret.append(np.log(data[n+1])-np.log(data[n]))
                
                ku.append(kurt(ret,fisher=True))
                
            pl.plot(x,ku,'.',color='grey')
            pl.xlabel('Time scale [min]')
            pl.ylabel('Excess kurtosis')
                       
        
        pl.show()
                    
        
		
#=======================================================#
#                       MAIN                            #		
#=======================================================#

dados = market()
dados.plot(4)
pl.show()



	
