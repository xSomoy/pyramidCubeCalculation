base = int(input("how many cube's in base? "))
total = 0
layer = 0
while layer != base:
    total  = total + (base-layer)
    layer=layer+1
print("There are total " + str(total) + " Cubes") 