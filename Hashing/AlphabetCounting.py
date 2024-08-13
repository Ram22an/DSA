Frequency=[0]*123
# it can be reduce but with one condition like only small alphabet only
# like for upper case Frequency[65-ord(i)] or Frequency[ord(i-a)] 
String=input("Enter the string here ")
for i in String:
    Frequency[ord(i)]+=1
Query=int(input("Enter the number of query "))
for _ in range(Query):
    temp=input()
    print(Frequency[ord(temp)])
