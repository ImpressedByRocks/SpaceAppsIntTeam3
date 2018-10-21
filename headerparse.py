data = open("testdata.ascii","r")
counter = 0
for line in data:
    if counter == 100:
        break
    print(line)
    counter = counter + 1
