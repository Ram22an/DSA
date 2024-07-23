Height=int(input())
# triangle with * 
for i in range(Height):
    for j in range(i+1):
        print("*",end="")
    print("")
# triangle with number according to j
for i in range(Height):
    for j in range(i+1):
        print(j+1,end="")
    print("")
# triangle with number according to i 
for i in range(Height):
    for j in range(i+1):
        print(i+1,end="")
    print("")
