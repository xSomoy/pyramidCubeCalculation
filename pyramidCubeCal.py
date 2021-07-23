# Total Cube Calculation Based On The Number of Cube in a Base Layer
# By John Deadman 14:40 23/07/2021 +0600 GMT

base = int(input("How many cubes in base?\n"))
total = 0
layer = 0
while layer != base:
    total  = total + (base-layer)
    layer=layer+1
print("There are total " + str(total) + " cubes") 