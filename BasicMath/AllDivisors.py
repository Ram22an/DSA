x=int(input())
arr=[]
i=2
while i<=x**0.5:
    if x%i==0:
        arr.append(i)
        temp=x//i
        if temp not in arr:
            arr.append(x//i)
    i+=1
arr.sort()
print(" ".join(map(str,arr)))
