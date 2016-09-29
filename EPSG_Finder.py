# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 06:01:57 2016

@author: root
"""
EPSG = input('Please type in the wanted EPSG:\n')

if EPSG == "4326":
    print("EPSG Value ",EPSG," Corresponds to WGS84")
elif EPSG == "3067":
    print("EPSG value 3067 corresponds to ETRS-TM35FIN")
elif EPSG == "2392":
    print("EPSG value 2392 corresponds to KKJ/Finland zone2")
    
else:
    print("There are so many spatial references. I dont know them all sorry.")
    
'''
In first print EPSG i wanted to try different way of printing the EPSG value in
between text.
'''
    