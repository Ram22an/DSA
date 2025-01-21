Matrix=[]
ColumnIndex=set()
while True:
    row_input = input()
    if row_input.strip() == "":
        break
    row = list(map(int, row_input.split()))
    if 0 in row:
        zero_indices = [index for index, value in enumerate(row) if value == 0]
        ColumnIndex.update(zero_indices)
        Size=len(row)
        row[:]=[0]*Size
    Matrix.append(row)
SizeOfMatrix=len(Matrix)
print(ColumnIndex)
for i in range(SizeOfMatrix):
    for j in ColumnIndex:
        Matrix[i][j]=0
print(Matrix)
# this is an easy question 👆🏻
