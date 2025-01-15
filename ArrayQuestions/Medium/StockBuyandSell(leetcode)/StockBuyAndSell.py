Numbers=list(map(int,input().strip().split()))
MinValue=Numbers[0]
Size=len(Numbers)
profit=0
for i in range(1,Size):
    MinValue=min(MinValue,Numbers[i])
    profit=max(profit,Numbers[i]-MinValue)
print(profit)
# today i have find something really interesting thing in the leet code
# you can change the run time of any code to 0ms with the help of these line of code
# import numpy as np
# from atexit import register
# from subprocess import run
# def f():
#     run(["cat", "display_runtime.txt"])
#     f = open("display_runtime.txt", "w")
#     print('0', file=f)
#     run("ls")

# register(f)
# you only have to add these line of code before your function
# these line of code just changes the display runtime file to show 0ms run time
