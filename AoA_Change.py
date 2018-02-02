#!/usr/bin/python
import math  

# Function which calculates the coordinates of the airfoil at the new angle of attack.
def rotate(origin, point, angle): 
  
    ox, oy = origin 
    px, py = point  

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy) 
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy) 
    
    return qx, qy

# Open the .txt file that contains the airfoil coordinates at 0 angle of attack.
coordsAt0 = [] 
with open('coordinatesAt0.txt') as fin: 
    fin.readline() 
    for l in fin:     
        coords = map(float,l.split())
        angle = 30 # The angle of attack the airfoil will be rotated by, COUNTER-CLOCKWISE!
        origin = (0,0) # The origin where the airfoil will be rotated around.
        coords0 = rotate(origin, coords[:2], math.radians(angle))
        coordsAt0.append(coords0)
        
# Optionally, print the new coordinates in terminal. Can be used in conjuction with Dot2Comma.py for use in ANSYS Fluent Software.
        #print coords

# Output the new coordinates in .geo format for use in Gmsh.     
with open('newcoordinates.geo','w') as fout: 
    for i, c in enumerate(coordsAt0): 
        fout.write('Point (%i) = {%f, %f, 0, 1};\n'%(i+1,c[0],c[1]))

