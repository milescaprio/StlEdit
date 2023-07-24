import numpy
from stl import mesh
import math

UNIT = 10;
# Using an existing stl file:
your_mesh = mesh.Mesh.from_file('inputa.stl')

m = 0;
while True:
    try:
        for p in range(9):
            your_mesh[m][p] = your_mesh[m][p]*abs(your_mesh[m][p])
            your_mesh[m][p] *= UNIT
    except:
        break
    m += 1;
#your_mesh.rotate([0, 1, 0], math.radians(45),)# point=[500, 2, 3])
#your_mesh.rotate([1, 0, 0], math.radians(45),)# point=[500, 2, 3])
#your_mesh.x+=100

your_mesh.save('new_stl_file.stl')
