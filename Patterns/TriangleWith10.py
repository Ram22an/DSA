x=int(input())
for i in range(x):
    start=1
    if i%2!=0:
        start=0
    else:
        start=1
    for j in range(i+1):
        print(start,end="")
        # try this 
        # it is drive from start=a+b-start
        start=1-start
        # this is noob statement
        # if start==0:
        #     start=1
        # else:
        #     start=0
    print()
