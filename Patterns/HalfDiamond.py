height=int(input())
for i in range(2*height-1):
    if i<height:
        for j in range(i+1):
            print("*",end="")
        print(" ",end="")
    else:
        # i-height,height
        for j in range(2 * height - 1 - i):
            print("*",end="")
        print(" ",end="")
    print("1")
