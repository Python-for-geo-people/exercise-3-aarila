# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 06:33:46 2016

@author: root
"""
star = "*"
text = ""
line = "-"  
    
for y in range(5):
    if y < 3:
        for x in range(7):
            text += star
        for z in range(12):
            text += line
        text += "\n"
    else:
        for j in range(19):
            text += line
        text += "\n"
        
print(text)          
        
        
     