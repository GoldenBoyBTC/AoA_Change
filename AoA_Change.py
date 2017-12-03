#!/usr/bin/python

import math  

def rotate(origin, point, angle): 
  
    ox, oy = origin 
    px, py = point  

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy) 
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy) 
    
    return qx, qy

coordsAt0 = [] 
with open('coordinatesAt0.txt') as fin: 
    fin.readline() 
    for l in fin:     
        coords = map(float,l.split())
        angle = 90 # degrees
        origin = (0,0)
        coords0 = rotate(origin, coords[:2], math.radians(angle))
        coordsAt0.append(coords0)

with open('newcoordinates.geo','w') as fout:
    for i, c in enumerate(coordsAt0):
        fout.write('Point (%i) = {%f, %f, 0, 1};\n'%(i+1,c[0],c[1])) 

