# here we have done kind of backtracking
def Print1toN(n):
    if n<1:
        return
    Print1toN(n-1)
    print(n)
x=int(input())
Print1toN(x)
