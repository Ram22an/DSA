import ast
IntervalString=input()
IntervalList=ast.literal_eval(IntervalString)
Size=len(IntervalList)
Ans=[]
IntervalList.sort()
if Size>1:
    for i in range(Size):
        if i>0:
            if Ans[-1][-1]>=IntervalList[i][0]:
                Ans[-1][-1]=max(IntervalList[i][-1],Ans[-1][-1])
            else:
                Ans.append([IntervalList[i][0],IntervalList[i][-1]])
            # if IntervalList[i-1][-1]>=IntervalList[i][0]:
            #     Ans.append([IntervalList[i-1][0],IntervalList[i][-1]])
            # else:
            #     Ans.append([IntervalList[i][0],IntervalList[i][-1]])
        else:
            Ans.append([IntervalList[i][0],IntervalList[i][-1]])
else:
    Ans=IntervalList[:]
print(Ans)
# this is not giving correct answer
# after changes it is working
# not working one is this one 👇🏻
# class Solution:
#     def merge(self, IntervalList: List[List[int]]) -> List[List[int]]:
#         Size=len(IntervalList)
#         Ans=[]
#         IntervalList.sort()
#         IntervalList.sort()
#         if Size>1:
#             for i in range(1,Size):
#                 if IntervalList[i-1][-1]>=IntervalList[i][0]:
#                     Ans.append([IntervalList[i-1][0],IntervalList[i][-1]])
#                 else:
#                     Ans.append([IntervalList[i][0],IntervalList[i][-1]])
#         else:
#             Ans=IntervalList[:]
#         return Ans
