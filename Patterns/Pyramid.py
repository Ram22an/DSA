Height=int(input())
# for this we are using this formula 
# for n number of rows there are 2n-1 columns
for i in range(Height):
    for j in range(2*Height-1):
        if Height - 1 - i <= j <= Height - 1 + i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
