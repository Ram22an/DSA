x=int(input())
space=2*(x)
for i in range(1,x+1):
    for j in range(1,i+1):
        print(f"{j}",end="")
    for j in range(1,space-1):
        print(" ",end="")
    for j in range(i,0,-1):
        print(f"{j}",end="")
    space-=2
    print()
