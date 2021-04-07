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

#---------------------------------------
# DESCRIPTION
#
# nret: Returns the normalized returns
#---------------------------------------

def nret(series):
    m = np.average(series)
    s = np.std(series)
    
    return [(r-m)/s for r in series]
    
    
