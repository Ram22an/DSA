x=int(input())
counter=0
while x!=0:
    counter=counter*10+x%10
    x=x//10
print(counter)
# this is simple for any number without trialing zeros
# this is the will work correctly for all the cases
x1=input()
reversed_x=""
for i in range(len(x1) - 1, -1, -1):
    reversed_x += x1[i]
print(reversed_x)
