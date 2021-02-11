f=open('Data','r')

#print(f.readline(),end=" ")

f1=open('abc','w')
f1.write("Something")

#Transfer information in Data to abc
for data in f:
    f1.write(data)
