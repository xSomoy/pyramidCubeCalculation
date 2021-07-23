base = input()
base = int(base)
total = 0
n=1
while n < base:
    total = base + (base-n)
    n=n-1
print(total) 