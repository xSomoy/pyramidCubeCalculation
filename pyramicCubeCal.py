base = input()
base = int(base)
n=1
while n < base:
    base = base + (base-n)
    n=n-1
print(base) 