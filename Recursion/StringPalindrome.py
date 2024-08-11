def ReverseString(String1,i,Size):
    if i>=Size-1-i:
        return
    temp=String1[i]
    String1[i]=String1[Size-1-i]
    String1[Size-1-i]=temp
    return ReverseString(String1,i+1,Size)
String=list(input())
# here i have learned about if i am writing like temp=String
# when i am changing any string both are changed
temp=String[:]
# so we can counter it by making a container by and putting the same content but pointing to different object
ReverseString(temp,0,len(String))
if temp==String:
    print("It is a palindrome string")
else:
    print("It is not a palindrome string")
