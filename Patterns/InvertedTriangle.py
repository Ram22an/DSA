Height=int(input())
# inverted triangle with *
for i in range(Height):
    for j in range(Height-i):
        print("*",end="")
    print("")
# inverted triangle with number according to j
for i in range(Height):
    for j in range(Height-i):
        print(j+1,end="")
    print("")
