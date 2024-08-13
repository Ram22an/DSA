# here is one constraine like if we enter 5 then array is of 5 size 
# and also element smaller than or equal to 5
Size=int(input())
Frequency=[0]*(10**8+1)
Arr=[]
for i in range(Size):
    temp=int(input())
    Arr.append(temp)
    Frequency[temp]+=1
print(Arr)
Query=int(input("Enter the number of query "))
for _ in range(Query):
    temp=int(input())
    print(Frequency[temp])
# print([f"{i} {index}"for i , index in enumerate (Frequency)])
