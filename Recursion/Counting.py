def PrintCountingRev(x):
    if x<=0:
        return
    print(x)
    x-=1
    PrintCountingRev(x)
def PrintCounting(x,Range):
    if x>Range:
        return
    print(x)
    x+=1
    PrintCounting(x,Range)
x=int(input())
counter=1
PrintCounting(counter,x)
print("-------------------------------------")
PrintCountingRev(x)
