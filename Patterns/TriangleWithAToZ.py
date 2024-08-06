x=int(input())
Ascii=65
for i in range(1,x+1):
    for j in range(1,i+1):
        print(f" {chr(Ascii)} ",end="")
        Ascii+=1
    Ascii=65
    print()
