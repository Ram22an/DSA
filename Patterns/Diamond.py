Height=int(input())
for i in range(Height):
    for j in range(2*Height-1):
        if i<=Height//2-1:
            if Height - 1 - i <= j <= Height - 1 + i:
                print("*", end="")
            else:
                print(" ", end="")
        else:
            if i<=j<=2*Height-2-i:
                print("*",end="")
            else:
                print(" ",end="")
    print()