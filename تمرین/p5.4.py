A=[1]

for i in range(9):
    print(A)
    B=[1]
    for j in range(len(A)-1):
        B.append(A[j] + A[j+1])
    B.append(1)
    A=B 
    print()