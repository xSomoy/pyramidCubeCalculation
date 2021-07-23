# Pyramid Cube Calculation Based On The Number of Cube in a Base Layer
# By John Deadman 14:40 23/07/2021 +0600 GMT

total = int(input("How many cubes you have?\n"))
layer = 0
while layer <= total:
    total  = total-layer
    if layer == total:
        layer = layer
    else:
        layer=layer+1
print("There are total " + str(layer) + " layers") 