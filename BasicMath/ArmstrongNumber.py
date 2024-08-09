x=input()
Size=len(x)
x=int(x)
temp=x
Total=0
while temp>0:
    Total+=(temp%10)**Size
    temp=temp//10
if Total==x:
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")
