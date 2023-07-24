import numpy
from stl import mesh
import tkinter
from tkinter.filedialog import askopenfile

# Using an existing stl file:

UNIT = 10

your_mesh = mesh.Mesh.from_file(askopenfile().name)

sx = eval(input("How much X to scale"));
sy = eval(input("How much Y to scale"));
sz = eval(input("How much Z to scale"));

def xyz(num):
    if num == 0:
        return sx
    if num == 1:
        return sy
    if num == 2:
        return sz

m = 0;
while True:
    try:
        for p in range(9):
            #print(your_mesh[m][p])
            your_mesh[m][p] = your_mesh[m][p]*xyz(p%3)
            your_mesh[m][p] *= UNIT
    except:
        break
    m += 1;

your_mesh.save('output.stl')
print("saved output to directory as this python file");
