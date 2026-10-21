
a=[1,2,3,4,5]
b=[]
for v in a:
    b+=[v]
print(b)
while true:
    name=input(":")
    if name=='exit':
        break
    b+=[name]
    print(b)
