base = input()
base = int(base)
total = 0
layer=1
while layer < base:
    total  = base-layer
    layer=layer+1

# for layer is < base:
#     total = base + (base-layer)
#     layer=layer+1
print(total) 