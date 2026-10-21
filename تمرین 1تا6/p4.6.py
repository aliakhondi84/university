a=[1,2,3,4,5,6,7,8,9,10]
n=len(a)
for i in range(n // 2):
    temp=a[i]
    a[i]=a[n-1-i]
    a[n-1-i]=temp
print(a)