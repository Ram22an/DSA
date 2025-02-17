# it is just a searching algorithm in a limited search space
# for binary search array should be sorted

Arr=list(map(int,input().split()))
Arr.sort()
Target=int(input("Enter the number to be found "))
Left=0
Right=len(Arr)-1
found=False
# this iterative way to find target
while Left<=Right:
    Mid=(Left+Right)//2
    if Arr[Mid]==Target:
        print(Target,Arr.index(Target))
        found=True
        break
    elif Arr[Mid]>Target:
        Right=Mid-1
    else:
        Left=Mid+1
if not found:
    print(f"{Target} is not found in array")

# and its time complexity is O(log²(n))
