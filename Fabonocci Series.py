x=0
y=1
l=[0,1]
for i in range(8):
    z=x+y
    l.append(z)
    x=y
    y=z
print(l)

