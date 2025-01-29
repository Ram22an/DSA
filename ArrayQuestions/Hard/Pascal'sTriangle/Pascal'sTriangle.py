# there could be three types of triangle related to this problem

# first you are given column and row find the element 
# second you have to print the whole row by given row number
# third print whole triangle

# for first question just use n(Row)Cr(Column) formula nCr=n!/(r!*(n-r)!)
# import math
# Row, Column = map(int, input().strip().split())
# result = math.factorial(Row + Column) // (math.factorial(Row) * math.factorial(Column))
# print(result)
# OR
# Row,Column=map(int,input().strip().split())
# Row-=1
# Column-=1
# RowFactorial=1
# ColumnFactorial=1
# RowTemp,Columntemp=Row,Column
# while RowTemp>0:
#     RowFactorial*=RowTemp
#     RowTemp-=1
# while Columntemp>0:
#     ColumnFactorial*=Columntemp
#     Columntemp-=1
# RowColumn=Row-Column
# RowColumnTemp=RowColumn
# RowColumnFactorial=1
# while RowColumnTemp>0:
#     RowColumnFactorial*=RowColumnTemp
#     RowColumnTemp-=1
# print(int(RowFactorial/(ColumnFactorial*RowColumnFactorial)))
# OR
# n(Row)Cr(Column)=n*(n-r)!/r!*(n-r)!
# so simpley get factorial upto n>n-r
# Row,Column=map(int,input().strip().split())
# Row-=1
# Column-=1
# Ans=1
# for i in range(Column):
#     Ans=Ans*(Row-i)
#     Ans=Ans/(i+1)
# print(int(Ans))


# For Second problem you can use the above program to generate all the number with help 
# of increasing row like from nC1 to nCn
# Or Refer the picture and code below
# Row=int(input().strip())
# Row-=1
# Ans=1
# AnsList=[]
# AnsList.append(1)
# for i in range(1,Row):
#     Ans=Ans*(Row-i)
#     Ans=Ans//i
#     AnsList.append(Ans)
# print(AnsList)


# for third problem we will use the second problem answer
def FindRow(Row):
    Ans=1
    AnsList=[]
    AnsList.append(1)
    for i in range(1,Row):
        Ans=Ans*(Row-i)
        Ans=Ans//i
        AnsList.append(Ans)
    return AnsList
NumberOfRows=int(input().strip())
PascalTriangle=[]
for i in range(1,NumberOfRows+1):
    PascalTriangle.append(FindRow(i))
print(PascalTriangle)
# it is a tough question 
