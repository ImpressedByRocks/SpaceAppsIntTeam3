import numpy as np
matrix = np.zeros((3,5184))

xc = 0
yc = 0


string = ""
flag = False
data = open("C:\\spaceapps\\filtereddata.csv","r")

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
    if yc == 5183:
        break
    xc = 0
