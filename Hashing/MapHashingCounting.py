Dict={}
Arr=list(map(int,input().split()))
for i in range(len(Arr)):
    if Arr[i] not in Dict:
        Dict[Arr[i]]=1
    else:
        Dict[Arr[i]]+=1
Query=int(input("Enter the number of query here "))
for _ in range(Query):
    temp=int(input("Enter the number to be found "))
    if Dict.get(temp) is None:
        print("Element is not present")
    else:
        print(Dict.get(temp))
print(Dict)
