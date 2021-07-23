base = int(input())
total = 0
layer=0
while layer != base:
    total  = total + (base-layer)
    layer=layer+1
print(total) 