# actuall there is an euclidean algorithm
# it states that gcd(a,b)=gcd(a-b,b) where a>b 
# when we have to do it repeatedly for getting the gcd of both the number
def HCForGCD(x,y):
    if x==0:
        return y
    if y==0:
        return x
    if x>y:
        return HCForGCD(x-y,y)
    else:
        return HCForGCD(y-x,x)
x=int(input())
y=int(input())
temp=HCForGCD(x,y)
print(temp)
# here is the more improved version
while x>0 and y>0:
    if x>y:
        x%=y
    if y>x:
        y%=x
if x==0:
    print(y)
else:
    print(x)
