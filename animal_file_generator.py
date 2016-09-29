# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
basename = "animal"
filenames = ""

for number in range(31):
    filenames=filenames + "\n"+basename+"_"+str(number) + ".shp"

print(filenames)

"""
# toinen vaihtoehto, printtaa tiedostonimet
for number in range(31):
    print(basename+"_"+str(number))
"""

