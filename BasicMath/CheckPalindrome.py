x1=input()
reversed_x=""
for i in range(len(x1) - 1, -1, -1):
    reversed_x += x1[i]
if x1==reversed_x:
    print("yes")
else:
    print("no")
