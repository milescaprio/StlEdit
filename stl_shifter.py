import numpy
from stl import mesh
import tkinter
from tkinter.filedialog import askopenfile

# Using an existing stl file:

your_mesh = mesh.Mesh.from_file(askopenfile().name)

addx = int(input("How much X to shift"));
addy = int(input("How much Y to shift"));
addz = int(input("How much Z to shift"));

your_mesh.x += addx
your_mesh.y += addy
your_mesh.z += addz

your_mesh.save('output.stl')
print("saved output to directory as this python file");
