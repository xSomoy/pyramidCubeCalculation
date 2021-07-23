# Pyramid Cube Calculation Based On The Number of Cube in a Base Layer
# By John Deadman 20:03 23/07/2021 +0600 GMT

total = int(input("How many cubes you have?\n"))
layer = 0
while layer <= total:
    total  = total-layer
    layer=layer+1

if layer == total:
    print("There are total " + str(layer-1) + " layers and " + str(total) + " cubes remains.") 
else:
    print("There are total " + str(layer-1) + " layers and " + str(total) + " cubes remains.") 