Height=int(input())
for i in range(Height):
    for j in range(2*Height-1):
        if i<=j<=2*Height-2-i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
