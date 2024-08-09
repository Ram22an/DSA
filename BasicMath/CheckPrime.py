x=int(input())
if x==1:
    print("Neither Prime or Composite")
elif x==2 or x==3:
    print("Prime")
elif x%2==0 or x%3==0:
    print("Composite")
else:
    Prime=True
    i=5
    while i<x:
        if x%i==0 or x%(i+2)==0:
            print("Composite")
            Prime=False
            break
        i+=6
    if Prime:
        print("Prime")
