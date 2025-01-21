# Matrix=[]
# while True:
#     Row_Input=input()
#     if Row_Input.strip()=="":
#         break
#     Row=list(map(int,Row_Input.split()))
#     Matrix.append(Row)
# Rows=len(Matrix)
# Columns=len(Matrix[0])
# left=0
# right=Rows-1
# top=0
# Bottom=Columns-1
# ans=[]
# while top<=Bottom and left<=right:
#     # right
#     for i in range(left,right+1):
#         ans.append(Matrix[top][i])
#     top+=1
#     # Bottom
#     for i in range(top,Bottom+1):
#         ans.append(Matrix[i][right])
#     right-=1
#     # left
#     if top<=Bottom:
#         for i in range(right,left-1,-1):
#             ans.append(Matrix[i][Bottom])
#         Bottom-=1
#     # top
#     if left<=right:
#         for i in range(Bottom,top-1,-1):
#             ans.append(Matrix[i][left])
#         left+=1
# print(ans)
Matrix = []
while True:
    Row_Input = input()
    if Row_Input.strip() == "":
        break
    Row = list(map(int, Row_Input.split()))
    Matrix.append(Row)

if not Matrix:
    print([])
else:
    Rows = len(Matrix)
    Columns = len(Matrix[0])
    left = 0
    right = Columns - 1
    top = 0
    Bottom = Rows - 1
    ans = []

    while top <= Bottom and left <= right:
        # left to right
        for i in range(left, right + 1):
            ans.append(Matrix[top][i])
        top += 1

        # top to bottom
        for i in range(top, Bottom + 1):
            ans.append(Matrix[i][right])
        right -= 1

        if top <= Bottom:
            # right to left
            for i in range(right, left - 1, -1):
                ans.append(Matrix[Bottom][i])
            Bottom -= 1

        if left <= right:
            # bottom to top
            for i in range(Bottom, top - 1, -1):
                ans.append(Matrix[i][left])
            left += 1

    print(ans)
# it is a difficult question 
