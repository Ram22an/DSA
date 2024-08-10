def PrintNameRecursion(counter,x):
    if counter>=x:
        return
    print(f"{counter+1}. Raman")
    counter+=1
    PrintNameRecursion(counter,x)
x=int(input())
counter=0
PrintNameRecursion(counter,x)
