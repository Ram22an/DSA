x=int(input())
Cont=1
for i in range(1,x+1):
    for j in range(i):
        print(f" {Cont} ",end="")
        Cont+=1
    print()
