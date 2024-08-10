# here we have done kind of backtracking
def Print1toN(counter,x):
    if counter>x:
        return
    # first we are calling the function and then printing the counter
    Print1toN(counter+1,x)
    print(counter)
x=int(input())
counter=1
Print1toN(counter,x)
