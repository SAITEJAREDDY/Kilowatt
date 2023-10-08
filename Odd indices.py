user_input=input("Please enter values sperated by spaces")
l=user_input.split()
l=[int(i) for i in l]
for i in l:
    if l.index(i)%2==1:
        print(i)