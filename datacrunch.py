data = open("output.txt","r")
file = open("output2.txt", "w")
counter = 0
for line in data:
    if counter == 100:
        file.write(line)
        counter = 0
    counter = counter + 1
