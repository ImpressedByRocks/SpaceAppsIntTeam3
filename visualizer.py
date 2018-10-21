import sys
import os
import bpy
import numpy as np

def ClearAll():
    bpy.ops.object.select_all(action='DESELECT')
    for object in bpy.data.objects:
        object.select = True
        bpy.ops.object.delete()

def CreateVoxel(x,y,z,r,g,b):
    bpy.ops.mesh.primitive_cube_add(location=(x,y,z))
    bpy.context.scene.objects.active.scale = (.2,.2,.2)
    activeObject = bpy.context.active_object #Set active object to variable
    mat = bpy.data.materials.new(name="MaterialName") #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    bpy.context.object.active_material.diffuse_color = (r, g, b) #change color

ClearAll()
matrix = np.zeros((3,5184))

xc = 0
yc = 0


string = ""
flag = False
data = open("C:\\spaceapps\\filtereddata4.csv","r")

for line in data:
    for char in line:
        print(xc,yc)
        if xc == 2:
            break
        if char == "\\":
            flag = True
        if (flag == True and char == "t") or char == '\t':
            matrix[xc,yc] = float(string)
            #print(string)
            string = ""
            xc = xc + 1
            flag = False
        if char == ",":
            matrix[xc,yc] = float(string)
            #print(string)
            string = ""
            xc = xc + 1
            flag = False
        else:
            string = string + char
    yc = yc + 1
    if yc == 5182:
        break
    xc = 0


#x0 = matrix[0,0]
#y0 = matrix[1,0]

#for i in range(0, 5000):
#    matrix[0,i] = matrix[0,i] - x0
#    matrix[1,i] = matrix[1,i] - y0
#    print("")
for i in range(0,5000):
    CreateVoxel(matrix[0,i],matrix[1,i]/2,matrix[2,i]/2, 0, 0, 1)
