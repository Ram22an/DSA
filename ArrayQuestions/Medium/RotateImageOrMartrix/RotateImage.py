Matrix=[]
while True:
    row=input()
    if row.strip()=="":
        break
    Row=list(map(int,row.split()))
    Matrix.append(Row)
RowSize,ColumnSize=len(Matrix),len(Matrix[0])
TempMatrix = [[0] * RowSize for _ in range(ColumnSize)]
print(TempMatrix,RowSize,ColumnSize)
for i in range(RowSize):
    for j in range(ColumnSize):
        TempMatrix[j][RowSize-i-1]=Matrix[i][j]
Matrix[:]=TempMatrix[:]
print(Matrix)
# this is an easy question 👆🏻
